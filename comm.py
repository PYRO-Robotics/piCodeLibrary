from motors import *

class commObject(object):

	def __init__(self, pin1, pin2, baud):
		self.pin1 = pin1
		self.pin2 = pin2
		self.baud = baud
		self.input = []

	def getRaw(tag):
		try:
			return input[tag]
		except IndexError:
			return 0
