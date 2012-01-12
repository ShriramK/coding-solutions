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
		name,value,work = string.split(line.strip(),',')
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
    totalVal, totalWork = 0,0
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
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
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
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
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
		print end_time-start_time

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance
#It performs well until maxWork = 5 as it reaches approximately 1.2 seconds, and anything beyond it nearly triples or quadraples the time it took in the previous iteration

res = {}
max = -1
ans = None#(,) ()
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
	global max, ans
	start_time1 = time.time()
	#print 'start_time ', start_time1
	#get all list of subjects that satisfy condition
	for i in subjects.keys():
		start_time = time.time()
		#print 'start_time ', start_time
		#print 'DpAdvisor ', dpAdvisor
		if subjects[i][WORK] <= maxWork:
			res[tuple([i])] = subjects[i][VALUE]
			#print 'max ', max, 'ans ', ans
			if res[tuple([i])] > max:
				max = res[tuple([i])]
				ans = tuple([i])
			if subjects[i][WORK] < maxWork:
				if index < len(subjects) - 1:
					diff = maxWork - subjects[i][WORK]
					dpAdvisorHelper([i], li[index+1:], diff, subjects )
					end_time = time.time()		
					#print 'End Time ', end_time
					#print 'Difference ' , end_time - start_time					

		index += 1
	end_time = time.time()
	#print 'end_time ', end_time
	print 'Difference ' , end_time - start_time1, '\n'

	#max = -1
	subjectSet = []
	index = None
	#index = 0

	if len(res) >0:
		start_time = time.time()
		#print 'start_time ', start_time	
		"""
		for i in res.keys():
			#print ' i ', i
			if res[i] > max:
				max = res[i]
				index = i
		"""
		#print ' ans ' , ans
		index = ans
		if type(index) != tuple:
			subjectSet.append(index)
			subjectSet = tuple(subjectSet)
		else:
			subjectSet = index
		end_time = time.time()
		#print 'end_time ', end_time
		
		#print 'Difference ' , end_time - start_time
		for subject in subjectSet:
			#print 'subject', subject, ' len ' , len(subjectSet)
			#print 'subjectSet ' , subjectSet
			temp[subject] = subjects[subject]		
	else:
		temp = {}
	return temp

def dpAdvisorHelper( subSet, newList, newMaxWork, subjects ):
	#print 'subSet ', subSet , ' newList ', newList, ' newMaxWork ', newMaxWork
	## go through every value of newList
	global max, ans
	for i in range(len(newList)):
		#print 'Element  i', i
		subject = newList[i]
		newWork = subjects[subject][WORK]
		diff = newMaxWork - newWork
		if diff >= 0:#newWork <= newMaxWork:
			res[tuple([subject])] = subjects[subject][VALUE]
			resizeSet = subSet[:]
			resizeSet.append(subject)
			prev = subjects[subject][VALUE]
			if diff > 0: #if newMaxWork > newWork
				#not contains case				
				if not res.__contains__(tuple(sorted(resizeSet))):
					for index in range(len(resizeSet)-2,-1,-1):
						tempSubset = resizeSet[index:]
						tS = tuple(sorted(tempSubset))
						res[tS] = subjects[resizeSet[index]][VALUE] + prev
						prev = res[tS]
						#print 'prev ', prev,
						if prev > max:
							max = prev
							ans = tS
				if len(newList) > 1:
					dpAdvisorHelper(resizeSet, newList[i+1:], diff, subjects)
			elif diff == 0:
				if not res.__contains__(tuple(sorted(resizeSet))):
					newSubSet = tuple(sorted(resizeSet))
					cSubSet = tuple(sorted(subSet))
					res[newSubSet] = res[cSubSet] + subjects[subject][VALUE]
					#print 'res[newSubSet] ', res[newSubSet],
					if res[newSubSet] > max:
						max = res[newSubSet]
						ans = newSubSet
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
		selected = dpAdvisor(newDictionary, i+1)
		print 'res ', res	
		printSubjects(selected)
		end_time = time.time()
		print end_time-start_time
		res = {}
		print '****************** BF ****************'		
		start_time = time.time()
		#print start_time
		selected = bruteForceAdvisor(newDictionary, i+1)
		printSubjects(selected)
		end_time = time.time()
		print end_time-start_time
#dpTime()
smallCatalog = {'6.00': (16, 8), '1.00':(7,7),'6.01':(5,3),'15.01':(9,6)}
#smallCatalog = {'6.00': (16, 8), '1.00':(7,7),'6.01':(5,3),'15.01':(9,6), '9.00':(10,2)}
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
for i in range(31):#7):#(6):#(2,3):#6):#31):
	#print ' i ' , i
	"""
	print '******************************** '
	print ' Brute Force maxWork ', i+1
	selected1 = bruteForceAdvisor(newDict, i+1)
	printSubjects(selected1)
	"""
	print '******************************** '
	print ' D  P maxWork ', i+1
	selected = dpAdvisor(newDict, i+1)#15)
	printSubjects(selected)
	res = {}
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
