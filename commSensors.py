from comm import *

class baseCommSensor(object):

	def __init__(self, master, tag):
		self.master = master
		self.tag = tag

	def getRaw(self):
		return master.getRaw(tag)
