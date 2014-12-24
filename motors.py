from subsys.py import *
from motorSensors.py import *

class motor(object):

	def __init__(self, port, inverted):
		self.port = port
		if inverted == 0:
			self.inv = 1
		else:
			self.inv = -1
		self.power = 0
		self.powerLast = 0

	def getLast(self): #Used to check if power output has changed
		return self.powerLast

	def getPort(self)
		return self.port

	def checkPower(self) #Used to check power without forcing an update
		return self.power

class dumbMotor(motor):

	def __init__(self, references, port, inverted)
		self.master = references
		motor.__init__(self, port, inverted)

	def getPower(self):
		self.powerLast = self.power
		self.power =  master.getPower() * self.inv
		return self.power

class smartMotor(motor):

	def __init__(self, references, port, inverted, sensor)
		self.master = references
		self.sensor = sensor
		motor.__init__(self, port, inverted)
		self.position = 0

	def getPosition(self):
		self.position = sensor.getPosition()
		return self.position

	def resetPosition(self):
		sensor.resetPosition()
		self.position = 0

class masterSmartMotor(motor):

	def __init__(self, references, port, inverted, sensor)
		smartMotor.__init__(self, references, port, inverted, sensor)
