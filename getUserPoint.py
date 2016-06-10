def getUserPoint(userName):
        try:
                userScoreFile = open('userScores.txt', 'r')
                for line in userScoreFile:
                        content = line.split(',')
                        if content[0] == userName:
				print content[1]
                                userScoreFile.close()
                                return content[1]
		userScoreFile.close()
                return "-1"
        except IOError:
                print("\nFile userScore.txt not found. A new file will be created.")
                userScoreFile = open ('userScores.txt', 'w')
                userScoreFile.close()
                return "-1"

getUserPoint('Benny')
