# def binary_search(a_list, target):
# 	first = 0

# 	last = len(a_list) - 1

# 	while first <= last and not False:
# 		mid = (first + last) // 2
		
# 	 	if target == a_list[mid]:
# 	 		return True
# 	 	else:
# 	 		if target < a_list[mid]:
# 	 			last = mid - 1
# 	 		else:
# 	 			first = mid + 1
# 	return False


# a = [1, 3, 5, 6, 7]
# print binary_search(a, 2)

def binary_search_recursive(a_list, item):
	if len(a_list) == 0:
		return False
	else:
		mid = len(a_list) // 2
		if a_list[mid] == item:
			return True
		else:
			if item < a_list[mid]:
				return binary_search_recursive([a_list[:mid]], item)
			else:
				return binary_search_recursive(a_list[mid + 1:], item)
	return False
a = [1, 3, 5, 6, 7]
print binary_search_recursive(a, 6)
