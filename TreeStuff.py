from Item import Item

#ibahn

class Tree(Item):

	height = 0
	root = None
	
	def makeLeaf(self, string, number):
		leaf = Item.fill(string, number)
		return leaf

	def fillTree(self, start, leaf):
		if start == None:
			start = leaf
		else:
			if start.numberItem > leaf.numberItem:
				fillTree(start.rightLeaf, leaf)
			elif start.numberItem < leaf.numberItem:
				fillTree(start.leftLeaf, leaf)
			else:
				fillTree(start.leftLeaf, leaf)


	def printTree(self, leaf):
		if leaf != None:
			print(leaf.stringItem + " " + leaf.numberItem)
			printTree(leaf.rightLeaf)
			printTree(leaf.leftLeaf)
