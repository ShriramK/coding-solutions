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
    if len(subjects) == 0:
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
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

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
    bestSubset, bestSubsetValue = bruteForceAdvisorHelper(tupleList, maxWork, \
                                  0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
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
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i + 1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i + 1, bestSubset, bestSubsetValue, subset,
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
#It performs well until maxWork = 5 as it reaches approximately 1.2 seconds, and anything beyond it nearly triples or quadraples the time it took in the previous iteration

#it's a dictionary that maps list of subjects to sum of its values
res = {} #subscripting it gives a tuple of value and work
#res =[]

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
	temp, li = {}, list(subjects)
	index = 0
	
	#print ' subjects  ' , subjects
	start_time = time.time()
	print 'start_time ', start_time
	values = []
	works = []
	xvalue = len(subjects)
	yvalue = maxWork
	
	for item in subjects.keys():
		works.append(subjects[item][WORK])
		values.append(subjects[item][VALUE])
	#print 'works ', works

	for i in range(1, xvalue + 1):
		for j in range(1, yvalue + 1):
			#print i, j, '*', type(i), type(j)
			res[i, j] = [-1, []] #-1#res[i][j] = -1
	print
	listOfSubjects = subjects.keys()
	result = dpAdvisorHelper(works, values, len(subjects), maxWork, \
							listOfSubjects)
	for item in result[WORK]:
		temp[item] = subjects[item]
		
	end_time = time.time()
	print 'end_time ', end_time
	print 'Difference ' , end_time - start_time, '\n'
	#print 'length ', len(res)
	#print 'res ', res
	"""
	max = -1
	subjectSet = []
	index = 0
	#if len(res) >0:
	start_time = time.time()
	print 'start_time ', start_time	
	for i in res.keys():
		#print 'res[i] ' ,res[i], 'res[i][VALUE] ', res[i][VALUE]
		#print 'max ' , max, ' i ' , i
		if res[i] > max:#res[i][VALUE] > max:
			max = res[i]#[VALUE]
			index = i
	end_time = time.time()
	print 'end_time ', end_time

	print 'Difference ' , end_time - start_time
	if type(subjectSet) == 'list':
		for subject in subjectSet:
			temp[subject] = subjects[subject]
	else:
		temp ={}
	"""
	return temp

#return value: total Value accumulated so far, combination of subjects
def dpAdvisorHelper( works, values, length, maxWork, listOfSubjects ):
	bestSubSet = []
	difference = works[length - 1] - maxWork
	if not length or not maxWork:
		ret = [0, []]
	else:
		if res[length, maxWork][VALUE] == -1:
			if difference > 0:
				res[length, maxWork] = dpAdvisorHelper(works, values, \
														length - 1, maxWork, \
														listOfSubjects)
			elif difference <= 0:
				prevOne = dpAdvisorHelper(works, values, length - 1, maxWork,\
										 listOfSubjects)
				subResultOne = prevOne[:]
				newMaxWork = maxWork - works[length-1]
				prevTwo = dpAdvisorHelper(works, values, length - 1, \
											newMaxWork, listOfSubjects)
				subResultTwo = prevTwo[:]
				subResultTwo[VALUE] += values[length - 1]
				maxValue = max(subResultTwo[VALUE], subResultOne[VALUE])
				if maxValue == subResultTwo[VALUE]:
					bestSubSet.append(listOfSubjects[length - 1])	
					for subject in subResultTwo[WORK]:
						bestSubSet.append(subject)
				else:
					for subject in subResultOne[WORK]:
						bestSubSet.append(subject)
				res[length, maxWork] = [maxValue, bestSubSet]			
		ret = res[length, maxWork]
	return ret
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
		#if i == 30:
		print 'i', i
		print '******************* DP ***************'		
		start_time = time.time()
		#print start_time
		selected = dpAdvisor(newDictionary, i + 1)
		print 'res ', res	
		printSubjects(selected)
		end_time = time.time()
		print end_time-start_time
		res = {}
		print '****************** BF ****************'		
		start_time = time.time()
		#print start_time
		selected = bruteForceAdvisor(newDictionary, i + 1)
		printSubjects(selected)
		end_time = time.time()
		print end_time-start_time
#dpTime()
#smallCatalog = {'6.00': (16, 8), '1.00':(7,7),'6.01':(5,3),'15.01':(9,6)}
smallCatalog = {
				'6.00': (16, 8),
				'1.00': (7, 7),
				'6.01': (5, 3),
				'15.01': (9, 6),
				'9.00': (10, 2)
}
#smallCatalog = {'6.00':(4,4), '1.00':(2,2), '6.01':(3,3), '15.01':(1,1)}
#smallCatalog = {'6.00':(1,1), '1.00':(2,2), '6.01':(3,3), '15.01':(4,4)}
#print greedyAdvisor(smallCatalog, 15, cmpValue)
#l = [ cmpValue, cmpWork, cmpRatio ]
#for i in l:
	#print greedyAdvisor(smallCatalog, 15, i)#cmpWork)#cmpValue)

#newDict = smallCatalog
newDict = loadSubjects("subjects.txt")
"""
for i in l:
	print 'i ', i
	selected = greedyAdvisor(newDict, 4, i)#cmpWork)#cmpValue)
	printSubjects(selected)
"""

#bruteForceTime()
#print dpAdvisor(smallCatalog, 16)
for i in range(1, 31):#22):#31):#(10,15):#15):#7):#20):#(31):#16):#(10):
#(6):#(15)
	"""
	print ' maxWork ' , i
	print '******************************** '
	print ' Brute Force maxWork ', i
	selected1 = bruteForceAdvisor(newDict, i)
	printSubjects(selected1)
	"""
	print '******************************** '
	print ' D  P maxWork ', i
	selected = dpAdvisor(newDict, i)#15)
	printSubjects(selected)
	res = {}#[]#{}
"""
newDictionary = loadSubjects("subjects.txt")
for i in range(31):
	start_time = time.time()
	#print start_time
	selected = dpAdvisor(newDictionary, i+1)
	printSubjects(selected)
	end_time = time.time()
	print end_time-start_time
	res = {}
"""
# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.
