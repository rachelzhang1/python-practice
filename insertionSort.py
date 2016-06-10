def insertion_sort(a_list):
	for index in range(1, len(a_list)):
		print "step1 begins"
		current_value = a_list[index]
		position = index
		
		print index
		print current_value
		
		print "step1 ends"

		while position > 0 and a_list[position - 1] > current_value:
			print "step2 begins"

			print ("position is:", position)
			print a_list[position - 1]
			print a_list[position]
			
			a_list[position] = a_list[position - 1]
			position = position - 1

			print a_list[position - 1]
			print a_list[position]
			print ("the new position is:", position)
			print "step2 ends"

		print "step3 begins"
		print position
		print ("a_list position now is:%d" %a_list[position])
		a_list[position] = current_value
	
		print "step3 ends"



a_list = [30, 50, 20, 10]
insertion_sort(a_list) 
#print (a_list)