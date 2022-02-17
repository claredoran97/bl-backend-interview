import unittest
from CommonPasswords import CommonPasswords
class UnitTest(unittest.TestCase):
	def testOneLetter():
		password = "z"
		expectedOutput = 6
		common = CommonPasswords(password)
		assert common.result == expectedOutput
	def testTooShort():
		password = "aA1"
		expectedOutput = 4
		common = CommonPasswords(password)
		assert common.result == expectedOutput
	def TestPass():
		password = "1377C0d3"
		expectedOutput = 0
		common = CommonPasswords(password)
		assert common.result == expectedOutput
	def testThreeConsecutiveLetters():
		password = "13777C0d3"
		expectedOutput = 1
		common = CommonPasswords(password)
		assert common.result == expectedOutput
	def testInCommonPasswordsExactly():
		password = "BvtTest123"
		expectedOutput = 1
		common = CommonPasswords(password)
		assert common.result == expectedOutput
	def testInCommonPasswords():
		password = "512345678yY"
		expectedOutput = 1
		common = CommonPasswords(password)
		assert common.result == expectedOutput
	def testContainsSymbols():
		password = "1234567--"
		expectedOutput = 3
		common = CommonPasswords(password)
		assert common.result == expectedOutput
	def testDoesNotContainUpperCase():
		password = "a67hhnp7t"
		expectedOutput = 1
		common = CommonPasswords(password)
		assert common.result == expectedOutput
	if __name__ == "__main__":
	    testOneLetter()
	    testTooShort()
	    TestPass()
	    testThreeConsecutiveLetters()
	    testInCommonPasswordsExactly()
	    testInCommonPasswords()
	    testContainsSymbols()
	    testDoesNotContainUpperCase()
