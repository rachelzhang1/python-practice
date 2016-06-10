import prime
import sys

if '/usr/rachel' not in sys.path:
	sys.path.append('usr/rachel')
answer = prime.checkIfPrime(13)
print (answer)
