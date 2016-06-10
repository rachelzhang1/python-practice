# hash table for integer - Remainder

def hash_int(a_int, table_size):
	return a_int % table_size


# hash table for strings with weighting. Solve the collisions for anangrams 
def hash(a_string, table_size): 
	sum = 0 
	for pos in range(len(a_string)):
		sum = sum + ord(a_string[pos]) * (pos + 1)
	return sum % table_size

# hash table: phone number and folding method (group in 2)

def hash_folding(a_list, table_size):
	sum = 0
	s = []
	s = a_list.replace('-', '', 2)

	for i in range(0, len(s), 2):
		sum = sum + int(s[i] + s[i+1])
	return sum % table_size

def hash_mid_square(a_int, table_size):
	s= str(pow(a_int, 2))
	i = len(s) / 2
	if len(s) % 2 == 0:
		return int(s[i-1]+s[i]) % table_size
	else:
		return int(s[i]) % table_size



print hash_int(77, 11)
print hash ("cat", 11)
print hash_folding("415-000-0099", 11)
print hash_mid_square(233, 11)
