class turntable(object):

	def __init__(self):
		self.rot = 0

	def setRot(self, rot)
		self.rot = rot

	def getRot(self)
		return self.rot

class xDrive(turntable):
	
	def __init__(self):
		turntable.__init__(self)
		self.lat = 0
		self.hor = 0

	def setLat(self, lat)
		self.lat = lat

	def getLat(self)
		return self.lat

	def setHor(self, hor)
		self.hor = hor

	def getHor(self)
		return self.hor

class xDriveWheel(object):

	def __init__(self, references, x, y):

		#   Wheel Pos
		#
		#  [0,0] [1,0]
		#
		#  [0,1] [1,1]
		
		self.master = references
		if x == 0:
			self.rot = 1
		else:
			self.rot = -1
		if y == 0:
			self.hor = self.rot
		else:
			self.hor = self.rot * -1
		self.power = 0

	def getPower(self)
		mRot = master.getRot()			
		mLat = master.getLat()
		mHor = master.getHor()
		self.power = mLat + mHor * self.hor + mRot * self.rot
		if self.power > 127:
			self.power = 127
		elif self.power < -127;
			self.power = -127
		return self.power
		
