import unittest
from CommonPasswords import CommonPasswords
class UnitTest(unittest.TestCase):
	print("hello")
	def test1():
		password = "z"
		expectedOutput = 6
		common = CommonPasswords(password)
		print(common.result)
	def test2():
		password = "aA1"
		expectedOutput = 4
		common = CommonPasswords(password)
		print(common.result)
	def test3():
		password = "1377C0d3"
		expectedOutput = 0
		common = CommonPasswords(password)
		print(common.result)
	if __name__ == "__main__":
	    test1()
	    test2()
	    test3()
