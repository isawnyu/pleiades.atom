import doctest
import unittest
from zope.testing import doctestunit
from zope.component import testing
from Testing import ZopeTestCase as ztc
from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
import pleiades.atom
from pleiades.atom.tests.base import PleiadesAtomFunctionalTestCase

ptc.setupPloneSite()

class TestCase(ptc.PloneTestCase):
    class layer(PloneSite):
        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            zcml.load_config('configure.zcml', pleiades.atom)
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            pass

#optionflags = (
#    doctest.NORMALIZE_WHITESPACE |
#    doctest.ELLIPSIS
#    )

def test_suite():
    return unittest.TestSuite([

        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='zgeo.plone.kml',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='zgeo.plone.kml.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        ztc.FunctionalDocFileSuite(
            'topic.txt', package='pleiades.atom.tests',
            test_class=PleiadesAtomFunctionalTestCase
            ),

        ztc.FunctionalDocFileSuite(
            'place.txt', package='pleiades.atom.tests',
            test_class=PleiadesAtomFunctionalTestCase
            ),
            
        ztc.FunctionalDocFileSuite(
            'place-gridsquare.txt', package='pleiades.atom.tests',
            test_class=PleiadesAtomFunctionalTestCase
            ),
            
        ztc.FunctionalDocFileSuite(
            'archive.txt', package='pleiades.atom.tests',
            test_class=PleiadesAtomFunctionalTestCase,
            #optionflags=optionflags
            ),
            
        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
