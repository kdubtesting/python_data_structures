class listItem:
	value = None
	nextItem = None

	def create(self, value):
		self.value = value
		return self

class recList:
	startItem = listItem();

	def addItem(self, loopItem, value):
		if loopItem.value == None:
			loopItem.value = value
			loopItem.nextItem = listItem()
		else:
			self.addItem(loopItem.nextItem, value);

	def loopThrough(self, through):
		if(through.value != None):
			print(through.value)
			self.loopThrough(through.nextItem);





if __name__ == '__main__':
	rl = recList()

	i = 0
	while i < 5:
		val = input("Enter a value: ")
		rl.addItem(rl.startItem, val)
		i += 1

	rl.loopThrough(rl.startItem)

	print(rl.startItem.nextItem.value)


	