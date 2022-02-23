import re
import ast
from collections import Counter
from itertools import groupby

class CommonPasswords():
	def __init__(self, password):
		self.password = password
		self.filePath = "../common-passwords.txt"
		self.fullList = []
		print()
		print(password)
		self.result = 0
		print()
		self.passwordChecks()


	def passwordChecks(self):
		print("lengthCheck")
		self.lengthCheck()
		print("occurenceCounter")
		self.occurenceCheckCounter()
		print("loadCommonPasswords")
		self.loadCommonPasswords()

	def lengthCheck(self):
		current_length = len(self.password)
		substituteString = "1Z8lx5P"
		print(current_length)
		if current_length < 7:
			difference = 7 - len(self.password)
			self.result += difference
			substituteString = substituteString[-difference:]
			self.password = self.password + substituteString
		elif current_length > 12:
			difference = len(self.password) - 12
			self.result += difference
			self.password = self.passwordst[:-difference]
		print(self.password)
		

	def checkContains(self, inputString):
		output = bool(re.match("(?=.*\d.*)(?=.*[a-z])(?=.*[A-Z])", inputString))
		return output
			# print("Contains more than just Numbers, Lower-Case Letters and Upper-Case Letters")

	def occurenceCounter(self):
		groups = groupby(self.password)
		result = [(label, sum(1 for _ in group)) for label, group in groups]
		print(result)
		newPassword = ""
		for key, value in result:
			if value >= 3:
				self.result += value - 2
			if value == 1:
				newPassword = newPassword + key
			else:
				newPassword = newPassword + key + key
		self.password = newPassword

	def occurenceCheckCounter(self):
		groups = groupby(self.password)
		result = [(label, sum(1 for _ in group)) for label, group in groups]
		print(result)
		newPassword = ""
		substituteString = "1Z8lx5P"
		for key, value in result:
			alpahnumeric = key.isalnum()
			if value >= 3:
				self.result += value - 2
				value = 2
			if (alpahnumeric == False):
				key = substituteString[1]
				substituteString = substituteString[:-1]
				self.result += value
			if value == 1:
				newPassword = newPassword + key
			else:
				newPassword = newPassword + key + key
		self.password = newPassword
		digitChange = False
		if(self.checkContains(self.password) == False and self.result < 2):
			if((not self.password.islower() and not self.password.isupper())==False and self.result == 0):
				self.result +=1
				digitChange = True
			if((any(i.isdigit() for i in self.password)) == False):
				if (self.result <= 1 and digitChange == True):
					self.result +=1
				elif(self.result == 0):
					self.result +=1

			print(self.password)
		

	def loadCommonPasswords(self):
		if self.fullList == []:
			with open(self.filePath, 'r') as infile:
				data = infile.read()
				self.fullList = data.splitlines()
		completeBool = False
		while(completeBool == False):
			result = [ele for ele in self.fullList if(ele in self.password)]
			if(result != []):
				print(result)
				smallestElment = min(result, key=len)
				self.result += 1
				if(smallestElment[-1] == "z"):
					newSmallest = smallestElment[:-1] + "1"
				else:
					newSmallest = smallestElment[:-1] + "z"
				self.password = self.password.replace(smallestElment, newSmallest)
			else:
				completeBool = True





	