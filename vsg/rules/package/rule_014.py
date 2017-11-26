
from vsg.rules.package import package_rule


class rule_014(package_rule):
    '''
    Package rule 014 checks for the package name exists on the same line as the "end" and "package" keywords.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '014'
        self.solution = 'End of package follows this format: end package <package name>.'
        self.phase = 1
        self.fixable = False  # User must add package name

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageEnd:
                lLine = oLine.lineLower.replace(';', '').split()
                if len(lLine) < 3 and lLine[1] == 'package':
                    self.add_violation(iLineNumber)
