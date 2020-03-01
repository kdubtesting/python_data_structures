from ListItems import ListItem
from TreeStuff import Tree

if __name__ == '__main__':

	choice = input("Tree or List: ")

	if choice.lower() == 't':
		tree = Tree();
		string = input("Enter a string: ")
		number = input("Enter a number: ")
		leaf = tree.makeLeaf(string, number)
		tree.fillTree(tree.root, leaf)

		tree.printTree(tree.root)
	else:
		startItem = None #Stationary pointer
		currentItem = None #Moving pointer
		size = 0

		while input("Do you want to write something? [y/N]").lower() == 'y':
			string = input("Enter a string here: ")
			number = input("Enter a number here: ")

			if size == 0:
				startItem = ListItem(string, int(number))
				currentItem = startItem
			else:
				item = ListItem(string, int(number))
				currentItem.add(item)
				currentItem = item

			size = size + 1

		loopItem = startItem

		while loopItem != None:
			print(loopItem.stringItem + " " + str(loopItem.numberItem))
			loopItem = loopItem.nextItem






