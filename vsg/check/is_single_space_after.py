'''
This module contains functions for rules to perform their checks.
'''

import re

from vsg.check import are_there_spaces_after

def is_single_space_after(self, sString, oLine, iLineNumber):
    '''
    Checks if a single space is after the string given.
    The string is considered a whole word.
    Allowances are made for end of line and semicolons.

    Parameters:

      self: (rule object)

      sString: (string)

      oLine: (line object)

      iLineNumber: (integer)
    '''

    are_there_spaces_after(self, sString, oLine, iLineNumber, 1)
#    sSpaces = ' ' * iSpaces
#    if not sString.lower() in oLine.lineLower:
#        return
#    if re.match('^.*' + sString + ';', oLine.lineLower):
#        return
#    if re.match('^.*' + sString + '$', oLine.lineLower):
#        return
#    if re.match('^.*' + sString + sSpaces + '\S', oLine.lineLower):
#        return
#    if not re.match('^.*\s+' + sString + sSpaces + '\S', oLine.lineLower) and \
#       not re.match('^\s*' + sString + sSpaces + '\S', oLine.lineLower) and \
#       not re.match('^.*\S\s' + sString + '\'', oLine.lineLower):
#        self.add_violation(iLineNumber)
