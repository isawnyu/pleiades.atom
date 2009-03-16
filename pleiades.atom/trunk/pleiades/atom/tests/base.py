from Products.Five import zcml
from Products.Five import fiveconfigure

from Testing import ZopeTestCase as ztc

from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

from pleiades.workspace.tests.base import ContentFunctionalTestCase

ztc.installProduct('ATVocabularyManager')
ztc.installProduct('Products.CompoundField')
ztc.installProduct('Products.ATBackRef')
ztc.installProduct('PleiadesEntity')

@onsetup
def setup_pleiades_atom():
    """Set up the additional products required for the Pleiades site policy.
    
    The @onsetup decorator causes the execution of this body to be deferred
    until the setup of the Plone site testing layer.
    """

    # Load the ZCML configuration for the optilux.policy package.
    
    fiveconfigure.debug_mode = True
    import pleiades.atom
    zcml.load_config('configure.zcml', pleiades.atom)
    fiveconfigure.debug_mode = False
    
    # We need to tell the testing framework that these products
    # should be available. This can't happen until after we have loaded
    # the ZCML.

    ztc.installPackage('pleiades.workspace')
    ztc.installProduct('zgeo.plone.geographer')
    ztc.installProduct('zgeo.plone.atom')    
    ztc.installPackage('pleiades.atom')
    
# The order here is important: We first call the (deferred) function which
# installs the products we need for the Pleiades package. Then, we let 
# PloneTestCase set up this product on installation.

setup_pleiades_atom()
ptc.setupPloneSite(
    products=[
    'ATVocabularyManager',
    'Products.CompoundField',
    'Products.ATBackRef',
    'PleiadesEntity',
    'pleiades.workspace',
    'zgeo.plone.geographer',
    'pleiades.atom'
    ])

class PleiadesAtomTestCase(ptc.PloneTestCase):
    """We use this base class for all the tests in this package. If necessary,
    we can put common utility or setup code in here.
    """

class PleiadesAtomFunctionalTestCase(ContentFunctionalTestCase):
    """We use this base class for all the tests in this package. If necessary,
    we can put common utility or setup code in here.
    """

    def afterSetUp(test):
        ContentFunctionalTestCase.afterSetUp(test)

        cid = test.portal.invokeFactory('Topic', id='places-topic')
        test.topic = test.portal[cid] 
        c = test.topic.addCriterion('portal_type', 'ATPortalTypeCriterion')
        c.setValue('Place')

        cid = test.portal.invokeFactory('Topic', id='features-topic')
        test.topic = test.portal[cid] 
        c = test.topic.addCriterion('portal_type', 'ATPortalTypeCriterion')
        c.setValue('Feature')

