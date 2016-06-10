from stackADT import Stack

def par_checker(syboml_string):
	s = Stack()
	balanced = True
	index = 0
	while index < len(syboml_string) and balanced:
		syboml = syboml_string[index]
		print syboml
		if syboml == '(':
			s.push(syboml_string)
#			print(s.peek())
		else:
			if s.is_empty():
				balanced = False
			else:
				s.pop()
#				print(s.peek())
		index = index + 1

	if balanced and s.is_empty():
		return True
	else:
		return False

#print(par_checker('((()))))'))
#print(par_checker('))(('))
print(par_checker('(())'))