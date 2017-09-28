# Problem Set 11: Simulating robots
# Name: Shriram Kunchanapalli
# Collaborators:
# Time: 6.30 PM, Dec'05 , 2011

import math
import random 

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
		"""
		Computes and returns the new Position after a single clock-tick has
		passed, with this object as the current position, and with the
		specified angle and speed.

		Does NOT test whether the returned position fits inside the room.

		angle: integer representing angle in degrees, 0 <= angle < 360
		speed: positive float representing speed

		Returns: a Position object representing the new position.
		"""
		old_x, old_y = self.getX(), self.getY()
		#print 'old_x ', old_x
		#print 'old_y ', old_y
		#print 'speed ', speed, 'angle ', angle
		# Compute the change in position
		delta_y = speed * math.cos(math.radians(angle))
		delta_x = speed * math.sin(math.radians(angle))
		# Add that to the existing position
		new_x = old_x + delta_x
		new_y = old_y + delta_y
		#print 'newx ' , new_x, ' newy ', new_y
		return Position(new_x, new_y)


# === Problems 1 and 2

class RectangularRoom(object):
	"""
	A RectangularRoom represents a rectangular region containing clean or dirty
	tiles.

	A room has a width and a height and contains (width * height) tiles. At any
	particular time, each of these tiles is either clean or dirty.
	"""
	def __init__(self, width, height):
		"""
		Initializes a rectangular room with the specified width and height.
		Initially, no tiles in the room have been cleaned.

		width: an integer > 0
		height: an integer > 0
		"""
		self.width = width
		self.height = height
		self.cleaned = 0
		self.tileArray = []
		for i in range(width):
			subTileArray = []
			for j in range(height):
				subTileArray.append(-1)
			self.tileArray.append(subTileArray)

	def cleanTileAtPosition(self, pos):
		"""
		Mark the tile under the position POS as cleaned.
		Assumes that POS represents a valid position inside this room.

		pos: a Position
		"""
		#print 'cleanTileAtPosition ',
		#print 'pos.getX() ', pos.getX(),
		#print 'pos.getY() ', pos.getY()
		self.tileArray[int(pos.getX()) - 1][int(pos.getY()) - 1] = 0
		self.cleaned += 1

	def isTileCleaned(self, m, n):
		"""
		Return True if the tile (m, n) has been cleaned.

		Assumes that (m, n) represents a valid tile inside the room.

		m: an integer
		n: an integer
		returns: True if (m, n) is cleaned, False otherwise
		"""
		return self.tileArray[int(m)][int(n)] == 0# pos.getX()][pos.getY()] == 0

	def getNumTiles(self):
		"""
		Return the total number of tiles in the room.

		returns: an integer
		"""
		return self.width * self.height

	def getNumCleanedTiles(self):
		"""
		Return the total number of clean tiles in the room.

		returns: an integer
		"""
		return self.cleaned
		# TODO: Your code goes here
	def getRandomPosition(self):
		"""
		Return a random position inside the room.

		returns: a Position object.
		"""
		return Position(random.randrange(0, self.width), \
						random.randrange(0, self.height))
	def isPositionInRoom(self, pos):
		"""
		Return True if POS is inside the room.

		pos: a Position object.
		returns: True if POS is in the room, False otherwise.
		"""
		xCoord = pos.getX()
		yCoord = pos.getY()
		return xCoord >= 0 and xCoord < self.width and yCoord >= 0 and \
				yCoord < self.height

class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    def __init__(self, room=None, speed=None): #define default values
		"""
		Initializes a Robot with the given speed in the specified
		room. The robot initially has a random direction d and a
		random position p in the room.

		The direction d is an integer satisfying 0 <= d < 360; it
		specifies an angle in degrees.

		p is a Position object giving the robot's position.

		room:  a RectangularRoom object.
		speed: a float (speed > 0)
		"""
		self.room = room
		self.speed = speed
		self.d = random.randrange(0, 360)
		self.p = room.getRandomPosition()
		# self.p = position
		positionObj = Position(random.randrange(0, self.room.width), \
								random.randrange(0, self.room.height))
		self.p = positionObj# self.room.getRandomPosition() gives a NoneType error

    def getRobotPosition(self):
		"""
		Return the position of the robot.

		returns: a Position object giving the robot's position.
		"""
		return self.p
    def getRobotDirection(self):
		"""
		Return the direction of the robot.

		returns: an integer d giving the direction of the robot as an angle in
		degrees, 0 <= d < 360.
		"""
		return self.d
    def setRobotPosition(self, position):
		"""
		Set the position of the robot to POSITION.

		position: a Position object.
		"""
		self.p = position
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.d = direction

class Robot(BaseRobot):
	"""
	A Robot is a BaseRobot with the standard movement strategy.

	At each time-step, a Robot attempts to move in its current
	direction; when it hits a wall, it chooses a new direction
	randomly.
	"""
	def __init__(self, room=None, speed=None): #whole init block added by me from inheritance e.g
		BaseRobot.__init__(self, room, speed)

	def updatePositionAndClean(self):
		"""
		Simulate the passage of a single time-step.

		Move the robot to a new position and mark the tile it is on as having
		been cleaned.
		"""
		oldPosition = self.p
		print 'self.d ', self.d,' self.speed ', self.speed
		newPosition = oldPosition.getNewPosition(self.d, self.speed)
		newDirection = self.d# None#random.randrange(0, 360)#-1
		triedDirections = []
		triedDirections.append(self.d)# newDirection)
		# check if position in room 
			# if in room
				# check if tile is not already cleaned
					# if not cleaned
						# break
					# else
						# getNewPosition
			# else 
				# getNewPosition
		
		while True:
			if self.room.isPositionInRoom(newPosition):
				# print 'In Room '
				if self.room.isTileCleaned(newPosition.getX(), \
											newPosition.getY()):
					# print 'Is Cleaned'
					newDirection = retrieveNewDirection(triedDirections)
					newPosition = oldPosition.getNewPosition(newDirection, \
															self.speed)
				else:
					# print 'Is not Cleaned'
					break
			else:
				# print 'Is not in Room'
				newDirection = retrieveNewDirection(triedDirections)
				newPosition = oldPosition.getNewPosition(newDirection, \
															self.speed)
			# print 'numCleaned' , self.room.getNumCleanedTiles(),
			# print 'size of triedDirection ', len(triedDirections)
				
		self.setRobotPosition(newPosition)
		self.setRobotDirection(newDirection)			
		self.room.cleanTileAtPosition(newPosition)

def retrieveNewDirection(triedDirections):
	# print 'triedDirections ', triedDirections
	newDirection = None
	while True:
		newDirection = random.randrange(0, 360)
		if newDirection in triedDirections:
			newDirection = random.randrange(0, 360)
		else:
			triedDirections.append(newDirection)		
			break
	return newDirection

# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, visualize):
	"""
	Runs NUM_TRIALS trials of the simulation and returns a list of
	lists, one per trial. The list for a trial has an element for each
	timestep of that trial, the value of which is the percentage of
	the room that is clean after that timestep. Each trial stops when
	MIN_COVERAGE of the room is clean.

	The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
	each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

	Visualization is turned on when boolean VISUALIZE is set to True.

	num_robots: an int (num_robots > 0)
	speed: a float (speed > 0)
	width: an int (width > 0)
	height: an int (height > 0)
	min_coverage: a float (0 <= min_coverage <= 1.0)
	num_trials: an int (num_trials > 0)
	robot_type: class of robot to be instantiated (e.g. Robot or
				RandomWalkRobot)
	visualize: a boolean (True to turn on visualization)
	"""
	# TODO: Your code goes here
	visualize = False
	totalAns = []
	totalTiles = width * height
	rRoom = RectangularRoom(width, height)	
	for robotObj in range(1, num_robots):
		robotObject = robot_type(rRoom, speed)
		ans = []
		for index in range(1, num_trials):
			subAns = []
			val = 0.0
			timeSteps = 0
			while val <= min_coverage:
				if val >= 0.8:
					print '*ASASDOSJDSAJSAJfjdfsjdlfjdslkgjdslkgjdslfdsfl'
				val += float(1) / totalTiles
				print 'val ', val, 'min_coverage ', min_coverage
				subAns.append(val)
				robotObject.updatePositionAndClean()
				timeSteps += 1
			ans.append(subAns)
		totalAns.append(ans)
	return totalAns

# create Robot object
rRoom = RectangularRoom(20, 20)# width, height)
# robotObj = Robot(rRoom, 20)	
avg = runSimulation(2, 1.0, 15, 20, 0.8, 5, Robot, False);

# === Provided function
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    if list_of_lists:
        longest = max([len(each_list) for each_list in list_of_lists])
    # Get totals
    tots = [0] * longest
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots / float(len(list_of_lists))
    return means


# === Problem 4
def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.
    """
    # TODO: Your code goes here

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    # TODO: Your code goes here

def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    # TODO: Your code goes here

def showPlot4():
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    # TODO: Your code goes here


# === Problem 5

class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """
    # TODO: Your code goes here


# === Problem 6

def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    """
    # TODO: Your code goes here
