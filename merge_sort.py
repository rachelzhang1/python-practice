def merge_sort(a_list):
	print("Splitting:", a_list)

	if len(a_list) > 1:
		mid = len(a_list) // 2
		left_half = a_list[:mid]
		right_half = a_list[mid:]
		# print left_half
		# print right_half
		# print a_list

		merge_sort(left_half)
		# print ("merge_sort1")
		# print left_half
		# print right_half
		# print a_list

		merge_sort(right_half)
		# print ("merge_sort2")
		# print left_half
		# print right_half
		# print a_list
		# print "####"

		i = 0
		j = 0
		k = 0
		
		# print left_half[0]
		# print right_half[0]
		# print a_list[k]

		while i < len(left_half) and j < len(right_half):

			# print ("While step 1")
			# print left_half[i], right_half[j], a_list[k]

			if left_half[i] < right_half[j]:
				a_list[k] = left_half[i]

				i = i + 1
				# print left_half[i]
				# print right_half[j]
				# print ("first k", a_list[k])
				# print i
			else:
				a_list[k] = right_half[j]
				j = j + 1
				# print ("l", left_half[i])
				
				# print ("k", a_list[k])
				# print j
			k = k + 1
			print k

		while i < len(left_half):
			# print ("While step 2")
			a_list[k] = left_half[i]
			i = i + 1
			k = k + 1
			
			# print i, k
			

		while j < len(right_half):
			# print ("While step 3")
			a_list[k] = right_half[j]
			j = j + 1
			k = k + 1
		
			
			# print j, k

	print("Merging", a_list)

a_list = [6, 5, 3]
merge_sort (a_list)
print a_list

