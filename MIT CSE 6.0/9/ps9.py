# 6.00 Problem Set 9
#
# Name: Shriram Kunchanapalli
# Collaborators:
# Time: 11:40 AM , 11/24/2011

import operator
import math
from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)

    def area(self):
        """
        Returns area of the square
        """
        return self.side ** 2

    def __str__(self):
        return 'Square with side ' + str(self.side)

    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)

    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159 * (self.radius**2)

    def __str__(self):
        return 'Circle with radius ' + str(self.radius)

    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
class Triangle(Shape):
	def __init__(self, h, b):
		"""
		h: height of the triangle
		b: base of the triangle
		"""
		self.height = float(h)
		self.base = float(b)

	def area(self):
		"""
		Returns approximate area of the triangle
		"""
		area_operand = reduce(operator.mul, [2, self.height, self.base])
		return pow(3, .5) / area_operand# x ** .5

	def __str__(self):
		return 'Triangle with base ' + str(self.base) + ' and ' + \
				str(self.height)

	def __eq__(self, other):
		"""
		Two triangles are equal if they have the same base and height.
		other: object to check for equality
		"""
		return type(other) == Triangle and self.base == other.base \
				and self.height == other.height

#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
	def __init__(self):
		"""
		Initialize any needed variables
		"""
		self.objList = []

	def addShape(self, sh):
		"""
		Add shape sh to the set; no two shapes in the set may be
		identical
		sh: shape to be added
		"""
		index = iter(self.objList)
		exists = False
		for index in self.objList:
			if index == sh:
				print 'Shape already exists'
				exists = True
				break
		if not exists:
			self.objList.append(sh)
		else:
			print 'Shape is not added to the set'

	def __iter__(self):
		"""
		Return an iterator that allows you to iterate over the set of
		shapes, one shape at a time
		"""
		return self.objList.__iter__()

	def __str__(self):
		"""
		Return the string representation for a set, which consists of
		the string representation of each shape, categorized by type
		(circles, then squares, then triangles)
		"""
		for item in self.objList:
			str(item)
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
	"""
	Returns a tuple containing the elements of ShapeSet with the
		largest area.
	shapes: ShapeSet
	"""
	iterator = iter(shapes)
	max_area = 0.0
	ans = []
	for iterator in shapes:
		if iterator.area() >= max_area:
			max_area = iterator.area()
	for iterator in shapes:
		if iterator.area() == max_area:
			ans.append(iterator)
	return tuple(ans)

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
	"""
	Retrieves shape information from the given file.
	Creates and returns a ShapeSet with the shapes found.
	filename: string
	"""
	inputFile = open(filename)
	obj = ShapeSet()
	cnt = 0
	for line in inputFile:
		cnt += 1
		data = split(line.strip(), ',')# string.split(line.strip(), ',')
		if len(data) == 3:
			obj.addShape(Triangle(data[1], data[2]))
		elif len(data) == 2:
			if data[0] == 'circle':
				obj.addShape(Circle(data[1]))
			else:
				obj.addShape(Square(data[1]))
	print cnt
	return obj

def test_ShapeSetAndFindLargest():
	print 'Testing ShapeSet class'
	ss = ShapeSet()
	ss.addShape(Triangle(1.2, 2.5))
	ss.addShape(Circle(4))
	ss.addShape(Square(3.6))
	ss.addShape(Triangle(1.6, 6.4))
	ss.addShape(Circle(2.2))
	largest = findLargest(ss)
	for item in largest:
		print item

def test_readShapesFromFile():
	dd = readShapesFromFile('shapes.txt')
	dd = sorted(dd)
	#print ss
	for item in dd:
		print item

test_ShapeSetAndFindLargest()
test_readShapesFromFile()
