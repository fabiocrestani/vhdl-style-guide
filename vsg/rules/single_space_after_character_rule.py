
from vsg import rule
from vsg import check
from vsg import fix


class single_space_after_character_rule(rule.rule):
    '''
    Single space after rule checks for a single space after a user specified keyword.
    '''

    def __init__(self, name=None, identifier=None, sTrigger=None, sWord=None):
        rule.rule.__init__(self, name=name, identifier=identifier)
        self.phase = 2
        self.sTrigger = sTrigger
        self.sWord = sWord
        self.solution = None

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.__dict__[self.sTrigger]:
            check.is_single_space_after_character(self, self.sWord, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = oFile.lines[dViolation['lineNumber']]
            fix.enforce_one_space_after_word(self, oLine, self.sWord)
