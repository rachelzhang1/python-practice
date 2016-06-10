#!/usr/bin/python
import time
class Fraction:
	def __init__(self, num, den):
		self.num = num
		self.den = den
#	my_fraction = Fraction(3, 5)

	def show(self):
		print(self.num, "/", self.den)
#my_f = Fraction(3, 5)
#my_f.show()
# print(my_f)

	def __str__(self):
		return str(self.num) + '/' + str(self.den)

my_f = Fraction(3, 5)
print(my_f)
print(my_f.__str__())
print(str(my_f))
#f = Fraction1(3, 5)
#print(f)
def sum_of_n(n):
	start = time.time()

	sum = 0
	for i in range(1, n+1):
		sum = sum + i

	end = time.time()
	return sum, end-start

print (sum_of_n(5))
for i in range(1,5):
	print ("Sum is %d required %10.7f seconds" %sum_of_n(10000))
#	print ("Sum is %d required %10.7f seconds" %sum_of_n(1000000))

def sum1(n):
	return (n*(n+1))/2
print(sum1(10))

#for i in range(1,5):
print("Sum is %d required %10.7f seconds" %sum1(10000))
#for i in range(1,5):
#	print ("Sum is %d required %10.7f seconds" %sum_of_n1(10000))

