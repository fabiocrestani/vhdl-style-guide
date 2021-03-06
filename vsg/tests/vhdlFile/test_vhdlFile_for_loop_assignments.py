import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','for_loop','for_loop_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testVhdlFileForLoopAssignments(unittest.TestCase):


    def test_isForLoopKeyword(self):
        lExpected = [9,19,21,26]
        lExpected.extend([36,40,44,48,52,56])
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isForLoopKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isForLoopEnd(self):
        lExpected = [11,23,24,28]
        lExpected.extend([38,42,46,50,54,58])
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isForLoopEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_ForLoopIndent(self):
        #           [   0,   1,2,   3,4,   5,6,7,   8,9,10,11,  12,13,   14]
        lExpected = [None,None,0,None,0,None,1,1,None,2, 3, 2,None, 1, None]
        # Generic actual list
        lActual = []
        iMaxCheck = len(lExpected)
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex == iMaxCheck:
                break
            lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isForLoopLabel(self):
        lExpected = [36,40,44,48,52,56]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isForLoopLabel:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
