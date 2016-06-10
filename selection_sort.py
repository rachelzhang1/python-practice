def selection_sort(a_list):
	for fill_slot in range (len(a_list) - 1, 0, -1):
		pos_max = 0
		

		for location in range (1, fill_slot + 1):
			if a_list[location] > a_list[pos_max]:
				pos_max = location

		print a_list[fill_slot]
		print a_list[pos_max]
		temp = a_list[fill_slot]
		a_list[fill_slot] = a_list[pos_max]
		a_list[pos_max] = temp
		print a_list[fill_slot]
		print a_list[pos_max]


	return a_list

a = [89, 10, 5, 68]
print selection_sort(a)

