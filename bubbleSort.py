def bubble_sort(a_list):
	for pass_num in range(len(a_list) - 1, 0, -1):
	#for pass_num in range(9, 0, -1):
		print ("round number:", pass_num)
		for i in range(pass_num):
			if a_list[i] > a_list[i+1]:
				# print i
				# print a_list[i], a_list[i+1]
				temp = a_list[i]
				a_list[i] = a_list[i+1]
				a_list[i+1] = temp
				# print a_list[i], a_list[i+1]
				# print a_list

	return a_list

# s = bubble_sort([5,2,3,4])
# print s
#print bubble_sort([4,5,3,1])
print bubble_sort([19,1,9,7,3,10,13,15,8,12])

def short_bubble_sort(b_list):
	exchange = True
	pass_num = len(b_list) - 1

	while pass_num > 0 and exchange:
		exchange = False

		for i in range(pass_num):
			#print i
			if b_list[i] > b_list[i+1]:
				print i
				print b_list[i], b_list[i+1]
				exchange = True
				temp = b_list[i] 
				b_list[i] = b_list[i+1]
				b_list[i+1] = temp
				print b_list[i], b_list[i+1]
		pass_num = pass_num - 1
	print pass_num
	return b_list

s2 = short_bubble_sort([3, 2, 1, 6])
print s2 