
import rule
import re


class architecture_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'architecture'


class rule_001(architecture_rule):
    '''Architecture rule 001 checks for spaces at the beginning of the line.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Remove spaces before architecture keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword:
                self._check_indent(oLine, iLineNumber)


class rule_002(architecture_rule):
    '''Architecture rule 002 checks for a single space between "architecture", "of", and "is" keywords.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Remove extra spaces after architecture keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword:
                if len(oLine.line.split()) > 4:
                    if not re.match('^\s*architecture\s\S+\sof\s\S+\sis', oLine.lineLower):
                        self.add_violation(iLineNumber)


class rule_003(architecture_rule):
    '''Architecture rule 003 checks for a blank line above the architecture keyword.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Add blank line above architecture keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword:
                self._is_blank_line_before(oFile, iLineNumber)


class rule_004(architecture_rule):
    '''Architecture rule 004 checks the architecture keyword is lower case.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change architecture keyword to lowercase.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword:
                if not re.match('^\s*architecture', oLine.line):
                    self.add_violation(iLineNumber)


class rule_005(architecture_rule):
    '''Architecture rule 005 checks if the "of" keyword is on the same line as the "architecture" keyword.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Change use keyword to lowercase.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword:
                lLine = oLine.lineLower.split()
                if len(lLine) < 3:
                    self.add_violation(iLineNumber)
                elif not lLine[2] == "of":
                    self.add_violation(iLineNumber)


class rule_006(architecture_rule):
    '''Architecture rule 006 checks if the "is" keyword is on the same line as the "architecture" keyword.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Change use keyword to lowercase.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword:
                lLine = oLine.lineLower.split()
                if len(lLine) < 5:
                    self.add_violation(iLineNumber)
                elif not lLine[4] == "is":
                    self.add_violation(iLineNumber)


class rule_007(architecture_rule):
    '''Architecture rule 007 checks for spaces at the beginning of the line for the "begin" keyword.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Remove spaces before "begin" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureBegin:
                self._check_indent(oLine, iLineNumber)


class rule_008(architecture_rule):
    '''Architecture rule 008 checks for spaces at the beginning of the line for the "end architecture" keywords.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Remove spaces before "end" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture:
                self._check_indent(oLine, iLineNumber)


class rule_009(architecture_rule):
    '''Architecture rule 009 checks for the "end" and "architecture" keyword are lower case.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Ensure "end" and "architecture" keywords are lower case.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture:
                if not re.match('^\s*end\s\s*architecture', oLine.line):
                    self.add_violation(iLineNumber)


class rule_010(architecture_rule):
    '''Architecture rule 010 checks for the entity name exists on the same line as the "end" and "architecture" keywords.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Add architecture name.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture:
                lLine = oLine.line.split()
                if len(lLine) > 2:
                    if lLine[2].startswith('--'):
                        self.add_violation(iLineNumber)
                else:
                    self.add_violation(iLineNumber)


class rule_011(architecture_rule):
    '''Architecture rule 011 checks the entity name is upper case on the closing "end architecture" line.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '011'
        self.solution = 'Uppercase architecture name.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture:
                lLine = oLine.line.split()
                if len(lLine) > 2:
                    if not lLine[2].startswith('--'):
                        self._is_uppercase(lLine[2], iLineNumber)


class rule_012(architecture_rule):
    '''Architecture rule 012 checks for a single space between the "end" and "architecture" keywords.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '012'
        self.solution = 'Single space between "end" and "architecture" keywords.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture:
                if (len(oLine.line.split()) > 1):
                    if not re.match('^\s*end\sarchitecture', oLine.lineLower):
                        self.add_violation(iLineNumber)


class rule_013(architecture_rule):
    '''Architecture rule 013 checks the architecture name is upper case in the architecture declaration.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '013'
        self.solution = 'Upper case architecture name.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword:
                if re.match('^\s*\S+\s\s*\S+\s\s*of\s\s*\S+\s\s*is', oLine.lineLower):
                    lLine = oLine.line.split()
                    self._is_uppercase(lLine[1], iLineNumber)


class rule_014(architecture_rule):
    '''Architecture rule 013 checks the entity name is upper case in the architecture declaration.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '014'
        self.solution = 'Upper case entity name.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword:
                if re.match('^\s*\S+\s\s*\S+\s\s*of\s\s*\S+\s\s*is', oLine.lineLower):
                    lLine = oLine.line.split()
                    self._is_uppercase(lLine[3], iLineNumber)


class rule_015(architecture_rule):
    '''Architecture rule 015 checks for a blank line below the architecture keyword.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '015'
        self.solution = 'Add blank line below architecture keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword:
                self._is_blank_line_after(oFile, iLineNumber)


class rule_016(architecture_rule):
    '''Architecture rule 016 checks for a blank line above the "begin" keyword.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '016'
        self.solution = 'Add blank line above the "begin" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureBegin:
                self._is_blank_line_before(oFile, iLineNumber)


class rule_017(architecture_rule):
    '''Architecture rule 017 checks for a blank line below the "begin" keyword.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '017'
        self.solution = 'Add blank line below the "begin" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureBegin:
                self._is_blank_line_after(oFile, iLineNumber)


class rule_018(architecture_rule):
    '''Architecture rule 018 checks for a blank line above the "end architecture" keywords.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '018'
        self.solution = 'Add blank line above the "end architecture" keywords.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture:
                self._is_blank_line_before(oFile, iLineNumber)