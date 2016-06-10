f = open ('myfile.txt', 'a')

#for line in f: 
#	print(line)

f.write('\nThis sentence will be appended.')

f.close()
