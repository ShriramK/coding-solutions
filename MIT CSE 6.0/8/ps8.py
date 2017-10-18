# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import sys
import time
import string
SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
	"""
	Returns a dictionary mapping subject name to (value, work), where the name
	is a string and the value and work are integers. The subject information is
	read from the file named by the string filename. Each line of the file
	contains a string of the form "name,value,work".

	returns: dictionary mapping subject name to (value, work)
	"""

	# The following sample code reads lines from the specified file and prints
	# each one.
	inputFile = open(filename)
	newDict = {}
	for line in inputFile:
		name, value, work = string.split(line.strip(), ',')
		newDict[name] = (int(value), int(work))
	return newDict
	# TODO: Instead of printing each line, modify the above to parse the name,
	# value, and work of each subject and create a dictionary mapping the name
	# to the (value, work).
	
	

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0, 0
    if not len(subjects):
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) + '\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res


def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2


def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
	"""
	Returns a dictionary mapping subject name to (value, work) which includes
	subjects selected by the algorithm, such that the total work of subjects in
	the dictionary is not greater than maxWork.  The subjects are chosen using
	a greedy algorithm.  The subjects dictionary should not be mutated.

	subjects: dictionary mapping subject name to (value, work)
	maxWork: int >= 0
	comparator: function taking two tuples and returning a bool
	returns: dictionary mapping subject name to (value, work)
	"""
	# TODO...
	# print subjects
	d, firstName, secondName, work, count = {}, None, None, maxWork, 0
	if comparator == cmpValue:
		# print 'CmpValue'
		maxValue = 0
		for i in subjects.keys():
			firstValue, firstWork, countS, tmp = subjects[i][VALUE], \
													subjects[i][WORK], 0, (0, 0)
			# print 'i ', i , 'firstValue ', firstValue, 'firstWork ', firstWork
			work -= firstWork
			for j in subjects.keys():
				# print 'j ', j
				if countS > count and subjects[j][WORK] <= work:
					# and countS >= 1:
					# print 'countS ', countS, ' count ', count,
					# print 'maxValue', maxValue
					# print subjects[j], tmp
					# print 'firstValue + tmp[VALUE] ', firstValue+tmp[VALUE]
					# print 'firstValue ', firstValue, 'tmp[VALUE] ', tmp[VALUE]
					if cmpValue(subjects[j], tmp) and \
						firstValue + tmp[VALUE] > maxValue:
						maxValue, firstName, secondName, tmp = \
							firstValue + tmp[VALUE], i, j, subjects[j]
				countS += 1
			work = maxWork
			count += 1
	elif comparator == cmpWork:
		# print 'CmpWork'
		minWork = sys.maxint
		for i in subjects.keys():
			firstValue, firstWork, countS = subjects[i][VALUE], \
											subjects[i][WORK], 0
			tmp = (sys.maxint, sys.maxint)
			work -= firstWork
			for j in subjects.keys():
				# print 'CountS, count, work, subjects[j][WORK]', countS,\
				# count, work, subjects[j][WORK]
				if countS > count and subjects[j][WORK] <= work:
					if cmpWork(subjects[j], tmp):
						if tmp[WORK] != sys.maxint:
							if firstWork + tmp[WORK] <= minWork:
								minWork, firstName, secondName, tmp = \
								   firstWork + tmp[WORK], i, j, subjects[j]
						else:
							tmp, firstName, secondName, minWork = subjects[j], \
													i, j, firstWork+tmp[WORK]
				countS += 1
			work = maxWork
			count += 1
	elif comparator == cmpRatio:
		# print '\nCmpRatio\n'
		maxRatio = 0
		for i in subjects.keys():
			# print 'i ', i
			firstValue, firstWork, countS, tmp = subjects[i][VALUE], \
										subjects[i][WORK], 0, (0, -1)
			# print 'i ', i , 'firstValue ', firstValue, 'firstWork ', firstWork
			work -= firstWork
			for j in subjects.keys():
				# print 'j ',j,' work', work, 'subjects[j][WORK] ',\
				# subjects[j][WORK]
				# print 'countS ', countS, ' count ' , count 
				if countS > count and subjects[j][WORK] <= work:
					# print 'tmp ', tmp#print 'i , j, tmp ', i , j, tmp
					if cmpRatio(subjects[j], tmp):
						first_ratio = float(firstValue) / firstWork						
						if tmp[WORK] > 0:
							# print 'maxRatio ', maxRatio
							# print 'firstvalue ',firstValue, 'firstWork ', \
							# firstWork, 'float(firstValue)/firstWork ', \
							# float(firstValue)/firstWork
							# print 'tmp        ',tmp[VALUE], tmp[WORK], \
							# float(tmp[VALUE])/tmp[WORK]
							temp_value = subjects[j][VALUE]
							temp_work = subjects[j][WORK]
							second_ratio = float(temp_value) / temp_work
							if first_ratio + second_ratio > maxRatio:
								maxRatio = first_ratio + second_ratio
								tmp, firstName, secondName = subjects[j], i, j
								# print ' Actual i , j ' , i , j
						else:
							# print 'Initial i, j ' , i , j
							tmp = subjects[j]
							if firstName is None:
								firstName, secondName = i, j
								tmp_ratio = float(tmp[VALUE]) / tmp[WORK]
								maxRatio = first_ration + tmp_ratio
				countS += 1
			work = maxWork
			count += 1
	print 'firstName', firstName, 'secondName', secondName
	d[firstName] = subjects[firstName]
	d[secondName] = subjects[secondName]
	return d

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = bruteForceAdvisorHelper(
    	                            tupleList, maxWork, 0, None,
    	                            None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset is None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(
            	    subjects, maxWork, i+1, bestSubset, bestSubsetValue,
            	    subset, subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(
        	    subjects, maxWork, i + 1, bestSubset, bestSubsetValue, subset,
        	    subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime():
	"""
	Runs tests on bruteForceAdvisor and measures the time required to compute
	an answer.
	"""
	# TODO...
	newDictionary = loadSubjects("subjects.txt")
	for i in range(10):
		print 'i', i
		start_time = time.time()
		print bruteForceAdvisor(newDictionary, i)
		end_time = time.time()
		print end_time - start_time

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance
# It performs well until maxWork = 5 as it reaches approximately 1.2 seconds,
# and anything beyond it nearly triples or quadraples the time it took in the
# previous iteration


res = {}


#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
	"""
	Returns a dictionary mapping subject name to (value, work) that contains a
	set of subjects that provides the maximum value without exceeding maxWork.

	subjects: dictionary mapping subject name to (value, work)
	maxWork: int >= 0
	returns: dictionary mapping subject name to (value, work)
	"""
	# TODO...
	temp, li = {}, list(subjects)  # equivalent to list(subjects.keys())
	# print 'list(subjects) ', list(subjects), ' maxWork ', maxWork
	# print 'len(subjects) ' ,len(subjects), '\n'
	index = 0
	for i in subjects.keys():
		if subjects[i][WORK] <= maxWork:
			# print 'TYPE ' ,type(i), i , ' in dpAdvisor '
			res[tuple([i])] = subjects[i][VALUE]
			if len(subjects) - index > 1:
				# print 'Entered \n'
				diff = maxWork - subjects[i][WORK]
				dpAdvisorHelper([i], li[index + 1:], diff, subjects)
		index += 1
	max_subject_value = -1
	subjectSet = []
	index = 0
	if len(res) > 0:
		for i in res.keys():
			"""if  i == ('6.00','7.16','7.17') or i == ('6.00','7.16') 
			or i == ('6.00','7.17') or i == ('7.16', '7.17'):
				print 'i ', i, ' res[i] ', res[i], ' * ',"""
			if res[i] > max_subject_value:
				max_subject_value = res[i]
				index = i
		if type(index) != tuple:
			subjectSet.append(index)
			subjectSet = tuple(subjectSet)
		else:
			subjectSet = index
		# print 'subjectSet ', subjectSet
		for subject in subjectSet:
			temp[subject] = subjects[subject]
		# print 'temp ', temp, 'maxWork ', maxWork
	else:
		temp = {}
	return temp


def dpAdvisorHelper(subSet, newList, newMaxWork, subjects):
	# print 'Entered , res ', res, '\n',
	for i in range(len(newList)):
		subject = newList[i]
		newWork = subjects[subject][WORK]
		if newWork <= newMaxWork:
			# print 'TYPE ', type(subject), subject
			res[tuple([subject])] = subjects[subject][VALUE]
			tempSubset = subSet[:]
			tempSubset.append(subject)
			'''if tempSubset == ['7.16', '7.17', '6.00']:
				print 'True or False ', \
				res.__contains__(tuple(sorted(tempSubset)))'''
			if not res.__contains__(tuple(sorted(tempSubset))):
				# lastSubject = subSet[len(subSet)-1]
				# print 'lastSubject ', lastSubject				
				tS = tuple(sorted(tempSubset))
				# print 'tempSubset ', tempSubset
				# print 'tS ', tS
				# print 'res ', res
				"""
				if type(subSet) == 'str':
					print 'subSet ', subSet, ' type ', type(subSet)	
					res[tS] = res[lastSubject] + subjects[newList[i]][VALUE]
				else:
				"""
				# print 'subSet ', subSet, ' type ', type(subSet)
				res[tS] = res[tuple(sorted(subSet))] + \
					subjects[newList[i]][VALUE]
				diff = newMaxWork - newWork
				if len(newList) > 1 and diff > 0:
					dpAdvisorHelper(tempSubset, newList[i+1:], diff, subjects)
	# print 'Exited \n'


#
# Problem 5: Performance Comparison
#
def dpTime():
	"""
	Runs tests on dpAdvisor and measures the time required to compute an
	answer.
	"""
	# TODO...
	newDictionary = loadSubjects("subjects.txt")
	for i in range(31):
		if i == 30:
			print 'i', i
			start_time = time.time()
			print start_time
			selected = dpAdvisor(newDictionary, i)
			printSubjects(selected)
			res = {}
			end_time = time.time()
			print end_time-start_time


smallCatalog = {
				'6.00': (16, 8),
				'1.00': (7, 7),
				'6.01': (5, 3),
				'15.01': (9, 6)
}
# smallCatalog = {'6.00':(4,4), '1.00':(2,2), '6.01':(3,3), '15.01':(1,1)}
# smallCatalog = {'6.00':(1,1), '1.00':(2,2), '6.01':(3,3), '15.01':(4,4)}
# print greedyAdvisor(smallCatalog, 15, cmpValue)
# l = [cmpValue, cmpWork, cmpRatio]
'''for i in l:
	print greedyAdvisor(smallCatalog, 15, i)#cmpWork)#cmpValue)'''

newDict = loadSubjects("subjects.txt")
# newDict = smallCatalog
"""
for i in l:
	print 'i ', i
	selected = greedyAdvisor(newDict, 4, i)#cmpWork)#cmpValue)
	printSubjects(selected)
"""

# bruteForceTime()
# print dpAdvisor(smallCatalog, 16)
for i in range(31):  # (6):#(2,3):#6):#31):
	# print ' i ' , i
	"""
	print '******************************** '
	print ' Brute Force maxWork ', i+1
	selected1 = bruteForceAdvisor(newDict, i+1)
	printSubjects(selected1)
	"""
	print '******************************** '
	print ' D  P maxWork ', i + 1
	selected = dpAdvisor(newDict, i + 1)  # 15)
	printSubjects(selected)
	res = {}

dpTime()
# print dpAdvisor(newDict, 5)#15)

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.
