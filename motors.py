from subsys.py import *

class motor(object):

	def __init__(self, port, inverted):
		self.port = port
		self.inverted = inverted
		self.power = 0

class dumbMotor(motor):

	def __init__(self, references, port, inverted)
		self.master = references
		motor.__init__(self, port, inverted)

	def getPower(self):
		self.power =  master.getPower()
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

	def resetPosition(self);
		sensor.resetPosition()
		self.position = 0

class masterSmartMotor(motor):

	def __init__(self, references, port, inverted, sensor)
		smartMotor.__init__(self, references, port, inverted, sensor)
