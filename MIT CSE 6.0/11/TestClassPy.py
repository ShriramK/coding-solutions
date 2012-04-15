class Room(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def updatePosition(self):
		pass

class Test1(object):
	def __init__(self, room, speed):
		self.room = room
		self.speed = speed

class Test2(Test1):
	def __init__(self):
		room = Room(-1, -1)
		Test1.__init__(self, room, speed="")
		pos = room.updatePosition()

roomObj = Room(1,2)
test1Obj = Test1(roomObj, 10)
test2Obj = Test2()