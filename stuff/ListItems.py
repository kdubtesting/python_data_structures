class ListItem:
	nextItem = None
	stringItem = ""
	numberItem = 0

	def __init__(self, string, number):
		self.stringItem = string
		self.numberItem = number

	def add(self, item):
		self.nextItem = item