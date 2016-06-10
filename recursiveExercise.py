def to_str(n, base):
	conver_string = "0123456789ABCDEF"
	if n < base:
		return conver_string[n]
	else:
		return to_str(n / base, base) + conver_string[n % base]
print(to_str(1453, 16))
print(to_str(10, 2))
print(to_str(10, 8))



from stackADT import Stack
r_stack = Stack()

def to_str_s(n, base):
	conver_string = "0123456789ABCDEF"
	while n > 0:
		if n < base:
			r_stack.push(conver_string[n])
		else:
			r_stack.push(conver_string[n % base])
		n = n // base

	res = ""
	while not r_stack.is_empty():
		res = res + str(r_stack.pop())
	return res

print(to_str_s(1453, 16))
