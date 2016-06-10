from linkedList import Node
from linkedList import UnorderedList
from linkedList import OrderedList

#temp = Node(93)
#print temp.get_data()

myList = UnorderedList()
myList.add(21)
myList.add(23)
myList.add(26)
myList.add(17)
myList.add(88)

#print myList.search(88)
#myList.remove(88)
#print myList.search(88)

myOrderedList = OrderedList()
myOrderedList.add(21)
myOrderedList.add(22)
myOrderedList.add(23)
myOrderedList.add(39)
myOrderedList.add(80)

print myOrderedList.search(22)
myOrderedList.remove(22)
print myOrderedList.search(22)





