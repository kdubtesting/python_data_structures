class Tree:
	root = {"item":None, "greater":None, "less":None}

	def addItem(self, item, start):
		if start["item"] == None:
			self.nodes += 1
			start["item"] = item
			start["greater"] = {"item":None, "greater":None, "less":None}
			start["less"] = {"item":None, "greater":None, "less":None}
		else:
			if start["item"][0] >= item[0]:
				self.addItem(item, start["greater"])
			else:
				self.addItem(item, start["less"])


if __name__ == "__main__":
	t = Tree()

	t.addItem("Hello", t.root)
	print(t.root["item"])

	t.addItem("Goodbye", t.root)
	print(t.root["greater"]["item"])

	t.addItem("Bye", t.root)
	print(t.root["greater"]["greater"]["item"])

	print(t.nodes)