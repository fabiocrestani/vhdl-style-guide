
import sys
sys.path.append('..\..')
import unittest
import rule_library
import os
import vhdlFile


# Read in test file used for all tests
oFile = vhdlFile.vhdlFile('library_test_input.vhd')
#oFile = []
#with open('library_test_input.vhd') as oFile:
#    for sLine in oFile:
#        oFile.append(sLine.rstrip())
#oFile.close()


class testRuleLibraryMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = rule_library.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '001')

        dExpected = [7,9,21]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = rule_library.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '002')

        dExpected = [13,20,21]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = rule_library.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '003')

        dExpected = [21]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = rule_library.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '004')

        dExpected = [9,20]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = rule_library.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '005')

        dExpected = [26,27,29]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = rule_library.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '006')

        dExpected = [27,29]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = rule_library.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '007')

        dExpected = [16,23,26,29]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = rule_library.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '008')

        dExpected = [14,16,26,29]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

if __name__ == '__main__':
    unittest.main()