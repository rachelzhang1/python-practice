from stackADT import Stack

def dec2Bin(dec_number):
	rem_stack = Stack()

	while dec_number > 0:
		rem = dec_number % 2
		rem_stack.push(rem)
		dec_number = dec_number // 2

	bin_string = ''
	while not rem_stack.is_empty():
		bin_string = bin_string + str(rem_stack.pop())

	return bin_string

print(dec2Bin(4))