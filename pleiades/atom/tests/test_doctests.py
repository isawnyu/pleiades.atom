import unittest
from Testing import ZopeTestCase as ztc
from Products.PloneTestCase import PloneTestCase as ptc
from pleiades.atom.tests.base import PleiadesAtomFunctionalTestCase

ptc.setupPloneSite()


def test_suite():
    return unittest.TestSuite([

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
            ),

        ])
