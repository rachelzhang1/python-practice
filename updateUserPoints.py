import os 

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

                os.remove('userScores.txt')
#                os.rename('userScores.tmp', 'userScores.txt')
updateUserPoints(False, 'Bear', '280')
