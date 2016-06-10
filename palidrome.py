from deque import Deque

def palidrome(aString):
	charDeque = Deque()

	for ch in aString:
		charDeque.add_rear(ch)

	stillEqual = True

	while charDeque.size() > 1 and stillEqual:
		#print charDeque.peek_front()
		first = charDeque.remove_front()
		#print charDeque.is_empty()
		#print charDeque.peek_rear()
		last = charDeque.remove_rear()

		if first != last:
			stillEqual = False

	return stillEqual


print(palidrome("lieagea"))
print(palidrome("radar"))