
from vsg.rules import indent_rule


class rule_001(indent_rule):
    '''
    Sequential rule 001 checks for the proper indentation at the beginning of the line.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'sequential', '001', 'isSequential')
