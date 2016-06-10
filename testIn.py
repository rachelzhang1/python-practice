def ordered_search(a_list, item):
	pos = 0
	while pos < len(a_list):
		if a_list[pos] == item:
			return True
		else:
			if a_list[pos] > item:
				return False
			else:
				pos = pos + 1
	return False

test_list = [1, 2, 5, 8, 10]
print ordered_search(test_list, 19)
print (test_list[:3])
print (test_list[3])