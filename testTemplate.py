class testInstance:
	'class to contain one test case'
	def __init__(self , inStr , outStr , str):
		self.inputStr  = inStr
		self.description = str
		self.outputStr = outStr
		
class testSuite:
	'test suite for adding bunch of related test cases'
	def __init__(self , str):
		self.count       = 0
		self.description = str
		self.instances   = []
		
	def add(self , instance):
		self.instances.append(instance)
		self.count=self.count+1
