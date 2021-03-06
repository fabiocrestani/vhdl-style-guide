
from vsg import rule
from vsg import fix

import re


class rule_002(rule.rule):
    '''
    Architecture rule 002 checks for a single space between "architecture", "of", and "is" keywords.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'architecture'
        self.identifier = '002'
        self.solution = 'Remove extra spaces after architecture keyword.'
        self.phase = 2

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isArchitectureKeyword and \
           len(oLine.line.split()) > 4 and \
           not re.match('^\s*architecture\s\S+\sof\s\S+\sis', oLine.lineLower):
            self.add_violation({'lineNumber': iLineNumber})

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            fix.enforce_one_space_after_word(self, oFile.lines[dViolation['lineNumber']], 'architecture')
            fix.enforce_one_space_before_word(self, oFile.lines[dViolation['lineNumber']], 'of')
            fix.enforce_one_space_after_word(self, oFile.lines[dViolation['lineNumber']], 'of')
            fix.enforce_one_space_before_word(self, oFile.lines[dViolation['lineNumber']], 'is')
