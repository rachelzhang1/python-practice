class Node:
	def __init__(self, init_data):
		self.data = init_data
		self.next = None

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_data(self, new_data):
		self.data = new_data

	def set_next(self, new_next):
		self.next = new_next

#temp = Node(93)
#print temp.get_data()
#print temp.get_next()


class UnorderedList:
	def __init__(self):
		self.head = None

	def is_empty(self):
		self.head == None

	def add(self, item):
		temp = Node(item)
		temp.set_next(self.head)
		self.head = temp

	def size(self):
		current = self.head
		count = 0

		while current != None:
			count = count + 1
			current = current.get_next()

		return count

	def search(self, item):
		current = self.head
		while current != None:
			if current.get_data() == item:
				return True
			else:
				current = current.get_next()
		return False

	def remove(self, item):
		current = self.head
		previous = None
		#found = False
		while current != None:
			if current.get_data() == item:
				#found = True
				#print ("I found it!","\n")
				break
			else:
				previous = current
				current = current.get_next()
				#found = False
				#print current.get_data()

		#if not found:
			#print ("I cannot find the item to remove","\n")

		if previous == None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())
		
		

class OrderedList:
	def __init__(self):
		self.head = None

	def is_empty(self):
		self.head == None

	def size(self):
		current = self.head
		count = 0

		while current != None:
			count = count + 1
			current = current.get_next()

		return count

	def search(self, item):
		current = self.head
		while current != None:
			if current.get_data() == item:
				return True
			else:
				if current.get_data() > item:
					return False
				else:
					current = current.get_next()
		return False

	def add(self, item):
		current = self.head
		previous = None

		while current != None:
			if current.get_data() > item:
				break
			else:
				previous = current
				current = current.get_next()

		temp = Node(item)

		if previous == None:
			temp.set_next(self.head)
			self.head = temp

		else:
			temp.set_next(current)
			previous.set_next(temp)

	def remove(self, item):
		current = self.head
		previous = None

		while current != None:
			if current.get_data() == item:
				break
			else:
				previous = current
				current = current.get_next()

		if previous == None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())









