import os

import unittest

from vsg.rules import library
from vsg import vhdlFile
from vsg.tests import utils


# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','library','library_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleLibraryMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = library.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '001')

        dExpected = utils.add_violation_list([7,9,21])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = library.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '002')

        dExpected = utils.add_violation_list([13,20,21])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = library.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '003')

        dExpected = [utils.add_violation(21)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = library.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '004')

        dExpected = [{'line_number': 9, 'words_to_fix': {'Library'}},
                     {'line_number': 20, 'words_to_fix': {'LIBRARY'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = library.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '005')

        dExpected = [{'line_number': 26, 'words_to_fix': {'USE'}},
                     {'line_number': 27, 'words_to_fix': {'Use'}},
                     {'line_number': 30, 'words_to_fix': {'uSe'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = library.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '006')

        dExpected = utils.add_violation_list([27,30])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = library.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '007')

        dExpected = utils.add_violation_list([16,23,26,30])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = library.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '008')

        dExpected = utils.add_violation_list([14,16,26,30])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
