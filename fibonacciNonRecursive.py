def f(n):
	
	my_list = [0, 1]

	for i in range (n):
		a = my_list[i] + my_list[i+1]
		my_list.append(a)

	return my_list.pop()

print f(4)