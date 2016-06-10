inputFile = open ('a.jpg', 'rb')
outputFile = open ('b.jpg', 'wb')

msg = inputFile.read(10)
while len(msg):
	outputFile.write(msg)
	msg = inputFile.read(10)

inputFile.close()
outputFile.close()
