class Queue:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)
	def peek(self):
		return self.items[len(self.items)-1]


def hotPotato(nameList, num):
	simQueue = Queue()
	for name in nameList:
		simQueue.enqueue(name)
	while simQueue.size() > 1:
		for i in range(num):
			print ("current i is %d" % (i))
			print "item on the front is " + simQueue.peek()
			simQueue.enqueue(simQueue.dequeue())
			print "after dequeue the front item, the front item becomes " + simQueue.peek()
		print "after 4 rounds, the front item is " + simQueue.peek()
		print simQueue.size()
		simQueue.dequeue()

	return simQueue.dequeue()

print(hotPotato(["Bill","David","Susan","Emily","Brad","Jane"], 7))
#print(hotPotato(["Bill","David"], 3))
# print(hotPotato(["A","B","C"], 4))
