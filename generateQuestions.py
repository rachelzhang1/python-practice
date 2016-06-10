import random as r

def generateQuestions():
	operandList = [0, 1, 2, 3, 4]
	operatorList = ['', '', '', '']
	operatorDict = {1:"+", 2: "-", 3: "*",4: "**"}
#i = len(operandList)
#j = 0
#while i:
#	if (i>0, j>= 0):
#		operandList[j] = randint(1, 9)
#		i -= 1
#		j += 1
#	print (operandList)
	for i in range(0,len(operandList)):
		operandList[i] = r.randint(1, 9)
		print(operandList)
		print (i)

#	for i in operandList:
#		i = r.randint(1, 9)
#		print i
#		print operandList

	for index in range(0,4):
		if index > 0 and operatorList[index-1]!='**':
#		if index>=0 and operatorList[index]!='**':
			operator = operatorDict[r.randint(1,4)]
			print operator
			print index
		else:
			operator = operatorDict[r.randint(1,3)]
			print index
			print operator
		operatorList[index] = operator
	questionString = str(operandList[0])

	for index in range(1, 5):
		questionString = questionString + operatorList[index-1] + str(operandList[index])
	result = eval(questionString)
	questionString = questionString.replace("**", '^')
	print('\n' + questionString )
	userResult = input('Answer:')
	while True:
		try:
			if int(userResult) == result:
				print("smart")
				return 1
			else:
				print("Wrong answer.")
				return 0
		except Exception as e:
			print("please input a correct number")
			userResult = input('Answer:')			
