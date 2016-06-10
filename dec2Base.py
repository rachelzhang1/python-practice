from stackADT import Stack

def dec2Base(dec_number, base):
	rem_stack = Stack()
	digits = "0123456789ABCDEF"

	while dec_number > 0:
		rem = dec_number % base
		rem_stack.push(rem)
		dec_number = dec_number // base

	bin_string = ''
	while not rem_stack.is_empty():
		bin_string = bin_string + digits[rem_stack.pop()]
		#print(digits(rem_stack.pop()))
		#print(rem_stack.pop())

	return bin_string

print(dec2Base(32,16))