import os

import unittest

from vsg.rules import file_statement
from vsg import vhdlFile
from vsg.tests import utils


# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'file_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleFileMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = file_statement.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'file')
        self.assertEqual(oRule.identifier, '001')

        dExpected = utils.add_violation_list([9,11,12])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = file_statement.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'file')
        self.assertEqual(oRule.identifier, '002')

        dExpected = [{'line_number': 9, 'words_to_fix': {'FILE'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = file_statement.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'file')
        self.assertEqual(oRule.identifier, '003')

        dExpected = [utils.add_violation(9)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003_w_5_spaces(self):
        oRule = file_statement.rule_003()
        oRule.spaces = 5

        dExpected = utils.add_violation_list([4,6,11,26])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
