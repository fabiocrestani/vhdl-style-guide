import os
import unittest

from vsg.rules import comment
from vsg import vhdlFile
from vsg import rule_list
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'comment_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)
lFileCase = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'comment_case_test_input.vhd'))
oFileCase = vhdlFile.vhdlFile(lFileCase)
lFileProcess = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'comment_process_test_input.vhd'))
oFileProcess = vhdlFile.vhdlFile(lFileProcess)
lFileLibrary = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'comment_library_test_input.vhd'))
oFileLibrary = vhdlFile.vhdlFile(lFileLibrary)
lFileIf = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'comment_if_input.vhd'))
oFileIf = vhdlFile.vhdlFile(lFileIf)


class testFixRuleCommentMethods(unittest.TestCase):

    def test_rule_010(self):
        oRule = comment.rule_010()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_003(self):
        oRule = comment.rule_003()
        dExpected = []
        oRule.fix(oFileProcess)
        oRule.analyze(oFileProcess)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = comment.rule_004()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = comment.rule_005()
        dExpected = []
        oRule.fix(oFileCase)
        oRuleIndex = comment.rule_010()
        oRuleIndex.fix(oFileCase)
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFileCase.lines[23].indentLevel, 3)
        self.assertEqual(oFileCase.lines[24].indentLevel, 3)
        self.assertEqual(oFileCase.lines[25].indentLevel, 3)

        self.assertEqual(oFileCase.lines[23].line, '      -- Comment 1')
        self.assertEqual(oFileCase.lines[24].line, '      -- Comment 2')
        self.assertEqual(oFileCase.lines[25].line, '      -- Comment 3')

    def test_rule_006(self):
        oRule = comment.rule_006()
        dExpected = []
        oRule.fix(oFileProcess)
        oRule.analyze(oFileProcess)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFileProcess.lines[37].line, '      variable a : integer 0 to 10;        -- comment')
        self.assertEqual(oFileProcess.lines[38].line, '      variable b : natural 0 to 256;       -- comment')

    def test_rule_001(self):
        oRuleList = rule_list.rule_list(oFileLibrary)
        oRuleList.fix(7)
        oRuleList.check_rules()

        self.assertEqual(oFileLibrary.lines[3].indentLevel, 1)
        self.assertEqual(oFileLibrary.lines[7].indentLevel, 1)

        self.assertEqual(oFileLibrary.lines[3].line, '  -- Comment 1')
        self.assertEqual(oFileLibrary.lines[7].line, '  -- Comment 1')

        oRuleList = rule_list.rule_list(oFileLibrary)
        oRuleList.check_rules()
        iExpectedFailures = 0
        iFailures = 0
        for oRule in oRuleList.rules:
            iFailures += len(oRule.violations)
        self.assertEqual(iFailures, iExpectedFailures)

    def test_rule_008(self):
        oRule = comment.rule_008()
        lExpected = []
        oRule.fix(oFileIf)
        oRule.analyze(oFileIf)
        self.assertEqual(oFileIf.lines[15].indentLevel, 2)
        self.assertEqual(oFileIf.lines[16].indentLevel, 2)
        self.assertEqual(oFileIf.lines[17].indentLevel, 2)

        self.assertEqual(oFileIf.lines[15].line, '    -- This is a comment')
        self.assertEqual(oFileIf.lines[16].line, '    -- to describe the elsif')
        self.assertEqual(oFileIf.lines[17].line, '    -- code')

        self.assertEqual(oFileIf.lines[20].indentLevel, 2)
        self.assertEqual(oFileIf.lines[21].indentLevel, 2)

        self.assertEqual(oFileIf.lines[20].line, '    -- Yet more code comments')
        self.assertEqual(oFileIf.lines[21].line, '    -- for the next elsif')

        self.assertEqual(oRule.violations, lExpected)

    def test_rule_009(self):
        oRule = comment.rule_009()
        lExpected = []
        oRule.fix(oFileIf)
        oRule.analyze(oFileIf)
        self.assertEqual(oFileIf.lines[24].indentLevel, 2)
        self.assertEqual(oFileIf.lines[25].indentLevel, 2)

        self.assertEqual(oFileIf.lines[24].line, '    -- and finally comments for the')
        self.assertEqual(oFileIf.lines[25].line, '    -- else code')

        self.assertEqual(oRule.violations, lExpected)
