from random import randint
from os import remove, rename

def getUserPoint(userName):
	try:	
		userScoreFile = open('userScores.txt', 'r')
		for line in userScoreFile:
			content = line.split(',')
			if content[0] == userName:
				userScoreFile.close()
				return content[1]
		userScoreFile.close()
		return "-1"
	except IOError:
		print("\nFile userScore.txt not found. A new file will be created.")	
		userScoreFile = open ('userScores.txt', 'w')
		userScoreFile.close()
		return "-1"
			
		
def updateUserPoints(newUser, userName, score):
	if newUser == True:
		input = open('userScores.txt', 'a')
		input.write('\n' + userName + ',' + score)
		input.close()
	else:
		input = open('userScores.txt', 'r')
		output = open ('userScores.tmp', 'w')
 		for line in input:
			content = line.split(',')
			if content[0] == userName:
				content[1] = score
				line = content [0] + ',' + content[1] + '\n'
			output.write(line)
		input.close()
		output.close()		
		
		remove('userScores.txt')
		rename('userScores.tmp', 'userScores.txt')

def generateQuestions():
        operandList = [0, 1, 2, 3, 4]
        operatorList = ['', '', '', '']
        operatorDict = {1:"+", 2: "-", 3: "*",4: "**"}
        
	for i in range(0,len(operandList)):
                operandList[i] = randint(1, 9)
                print(operandList)
		print i

        for index in range(0,len(operatorList)):
#	for index in range(0,4):
                if index > 0 and operatorList[index-1]!='**':
                        operator = operatorDict[randint(1,4)]
			print index
			print operator
                else:
                        operator = operatorDict[randint(1,3)]
			print index
			print operator
                operatorList[index] = operator
        questionString = str(operandList[0])
	print questionString

        for index in range(1, len(operandList)):
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

