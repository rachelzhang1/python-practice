try:

	import myPythonFunctions as m

	userName = input("Your name: \n")
	userScore = int(m.getUserPoint(userName))

	if userScore == -1:
		newUser = True
		userScore = 0
	else:
		newUser = False
	userChoice = 0
	while userChoice!='-1':
		userScore += m.generateQuestions()
		print("score", userScore)
		userChoice = input("Enter to Continue or -1 to Exit")
		print userChoice
	m.updateUserPoints(newUser, userName, str(userScore))

except Exception as e:
		print ("An unexpected error occurred. Program will be exited")

