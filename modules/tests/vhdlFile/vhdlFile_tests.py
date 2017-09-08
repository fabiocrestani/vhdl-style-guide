
import sys
sys.path.append('..\..')
import unittest
import vhdlFile

class testVhdlFileMethods(unittest.TestCase):

    def test_vhdlFile_class_exists(self):
        oFile = vhdlFile.vhdlFile('../rule_library/library_test_input.vhd')
        self.assertTrue(oFile)
        self.assertEqual(oFile.filename, '../rule_library/library_test_input.vhd')

    def test_loading_of_file(self):
        oFile = vhdlFile.vhdlFile('../rule_library/library_test_input.vhd')

        # Read in test file used for all tests
        lExpected = ['']
        with open('../rule_library/library_test_input.vhd') as oExpectedFile:
            for sLine in oExpectedFile:
                lExpected.append(sLine.rstrip())
        oExpectedFile.close()
        # Compare
        for iIndex, oLine in enumerate(oFile.lines):
            self.assertEqual(oLine.line, lExpected[iIndex])

    def test_blank_line_assignment(self):
        oFile = vhdlFile.vhdlFile('../rule_library/library_test_input.vhd')

        # Compare
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex == 1 or iIndex == 2 or iIndex == 6 or iIndex == 8 or iIndex == 11 or \
               iIndex == 12 or iIndex == 15 or iIndex == 17 or iIndex == 18 or iIndex == 19 or \
               iIndex == 22 or iIndex == 25 or iIndex == 28 or iIndex == 30:
                self.assertTrue(oLine.isBlank)
            else:
                self.assertFalse(oLine.isBlank)

    def test_library_assignment(self):
        oFile = vhdlFile.vhdlFile('../rule_library/library_test_input.vhd')
        lExpected = [3,7,9,13,20,21]
        # Compare
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex in lExpected:
                self.assertTrue(oLine.isLibrary)
                self.assertEqual(oLine.indentLevel, 0)
            else:
                self.assertFalse(oLine.isLibrary)

    def test_library_use_assignment(self):
        oFile = vhdlFile.vhdlFile('../rule_library/library_test_input.vhd')
        lExpected = [4,5,10,14,16,23,24,26,27,29]
        # Compare
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex in lExpected:
                self.assertTrue(oLine.isLibraryUse)
                self.assertEqual(oLine.indentLevel, 1)
            else:
                self.assertFalse(oLine.isLibraryUse)

    def test_insideEntity_assignment(self):
        oFile = vhdlFile.vhdlFile('../rule_entity/entity_test_input.vhd')
        lExpected = [0,1,2,17,18,48,64,79,92,93,104,105,106,107,108,109,110,111,112,124,125,126,134,135]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if not oLine.insideEntity:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEntityDeclaration_assignment(self):
        oFile = vhdlFile.vhdlFile('../rule_entity/entity_test_input.vhd')
        lExpected = [3,19,34,49,65,80,94,113,127]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isEntityDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndEntityDeclaration_assignment(self):
        oFile = vhdlFile.vhdlFile('../rule_entity/entity_test_input.vhd')
        lExpected = [16,33,47,63,78,91,103,123,133]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isEndEntityDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insidePortMap_assignment(self):
        oFile = vhdlFile.vhdlFile('../rule_port/port_test_input.vhd')
        lExpected = [8,9,10,11,12,13,14,15,25,26,27,28,29,30,31,39,40,41,42,43,44,45,46,56,57,58,59,60,61,62,70,71,72,73,74,75,76,77,86,87,88,89,90,98,99,100,101,102,118,119,120,121,122,128,129,130,131,132]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insidePortMap:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isPortKeyword_assignment(self):
        oFile = vhdlFile.vhdlFile('../rule_port/port_test_input.vhd')
        lExpected = [8,25,39,56,70,86,98,118,128]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isPortKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndPortMap_assignment(self):
        oFile = vhdlFile.vhdlFile('../rule_port/port_test_input.vhd')
        lExpected = [15,31,46,62,77,90,102,122,132]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isEndPortMap:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isPortDeclaration_assignment(self):
        oFile = vhdlFile.vhdlFile('../rule_port/port_test_input.vhd')
        lExpected = [9,10,11,12,13,14,26,27,28,29,30,31,40,41,42,43,44,45,57,58,59,60,61,62,71,72,73,74,75,76,87,88,89,99,100,101,119,120,121,129,130,131]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
if __name__ == '__main__':
    unittest.main()