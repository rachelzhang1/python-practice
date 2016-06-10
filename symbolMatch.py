from stackADT import Stack

def syb_checker(syboml_string):
	s = Stack()
	balanced = True
	index = 0
	while index < len(syboml_string) and balanced:
		syboml = syboml_string[index]
		print syboml
		if syboml in "([{":
			s.push(syboml)
#			print(s.peek())
		else:
			if s.is_empty():
				balanced = False
			else:
				top = s.pop()
				if not matches(top, syboml):
					balanced = False
#				print(s.peek())
		index = index + 1

	if balanced and s.is_empty():
		return True
	else:
		return False

def matches(open, close):
	opens = "([{"
	closes = ")]}"
	return opens.index(open) == closes.index(close)

#print(par_checker('((()))))'))
#print(par_checker('))(('))
print(syb_checker('({([])})'))