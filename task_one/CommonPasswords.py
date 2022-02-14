import re
from collections import Counter
class CommonPasswords():
	def __init__(self, password):
		self.password = password
		print(password)
		errorBool = True
		while errorBool == True:
			errorBool = self.lengthCheck()
			print(errorBool)
			# errorBool = False
			errorBool = self.checkContains()
			errorBool = self.occurenceCounter()
			errorBool = False
		self.result = 0

	def lengthCheck(self):
		current_length = len(self.password)
		print(current_length)
		if current_length < 7:
			return False
		elif current_length > 12:
			return False
		else:
			return True

	def checkContains(self):
		output = bool(re.match("(?=.*\d.*)(?=.*[a-z])(?=.*[A-Z])", self.password))
		print(output)
		return output

	def occurenceCounter(self):
		# This method is inefficient and doesnt work with succession issues
		res = Counter(self.password)
		print(res)
		return False

	