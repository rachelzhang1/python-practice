import random
from queue import Queue

class Printer:
	def __init__(self, ppm):
		self.page_rate = ppm
		self.current_task = None
		self.time_remaining = 0

	def tick(self):
		if self.current_task != None:
			self.time_remaining = self.time_remaining - 1
			if self.time_remaining <= 0:
				self.current_task = None

	def busy(self):
		if self.current_task != None:
			return True
		else:
			return False

	def startNext(self, new_task):
		self.current_task = new_task
		self.time_remaining = new_task.getPages() * 60 / self.page_rate


class Task:
	def __init__(self, time):
		self.timestamp = time
		self.pages = random.randrange(1, 21)

	def getStamp(self):
		return self.timestamp

	def getPages(self):
		return self.pages

	def waitTime(self, currentTime):
		return currentTime - self.timestamp


def simulation(numSeconds, pagePerMinute):

	labPrinter = Printer(pagePerMinute)
	printQueue = Queue()
	waitingTimes = []

	for currentSecond in range (numSeconds):

		if newPrintTask():
			task = Task(currentSecond)
			printQueue.enqueue(task)

		if (not labPrinter.busy()) and (not printQueue.is_empty()):
			nextTask = printQueue.dequeue()
			waitingTimes.append(nextTask.waitTime(currentSecond))
			labPrinter.startNext(nextTask)

		labPrinter.tick()

	averageWait = sum(waitingTimes)/len(waitingTimes)
	print("Average wait %6.2f secs %d taks remaining."%(averageWait, printQueue.size()))

def newPrintTask():
	num = random.randrange(1, 181)
	if num == 180:
		return True
	else: 
		return False

for i in range(10):
	simulation(3600, 5)
















