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

res = {} #subscripting it gives a tuple of value and work
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
	start_time1 = time.time()
	print 'start_time ', start_time1
	for i in subjects.keys():
		start_time = time.time()
		if subjects[i][WORK] <= maxWork:
			res[tuple([i])] = tuple([subjects[i][VALUE],subjects[i][WORK]])
			if subjects[i][WORK] < maxWork:
				if index < len(subjects) - 1:
					dpAdvisorHelper([i], li[index+1:], maxWork, subjects )
					end_time = time.time()
					break
		index += 1
	end_time = time.time()
	print 'end_time ', end_time
	print 'Difference ' , end_time - start_time1, '\n'

	print 'length ', len(res)
	
	max = -1
	subjectSet = []
	index = 0
	if len(res) >0:
		start_time = time.time()
		print 'start_time ', start_time	
		for i in res.keys():
			#print 'res[i] ' ,res[i], 'res[i][VALUE] ', res[i][VALUE]
			#print 'max ' , max, ' i ' , i
			if res[i][VALUE] > max:
				max = res[i][VALUE]
				index = i

		if type(index) != tuple:
			subjectSet.append(index)
			subjectSet = tuple(subjectSet)
		else:
			subjectSet = index
		end_time = time.time()
		print 'end_time ', end_time
		
		print 'Difference ' , end_time - start_time
		for subject in subjectSet:
			temp[subject] = subjects[subject]		
	else:
		temp = {}
	return temp

def dpAdvisorHelper( subSet, newList, newMaxWork, subjects ):
	ret = []
	if len(newList) > 1:
		prev = subSet
		cnt = 0
		index = 0
		for item in newList:
			itemWork = subjects[item][WORK]
			gap = newMaxWork - itemWork
			res[tuple([item])] = tuple([subjects[item][VALUE], itemWork])
			if gap == 0:
				subSet = None
			elif gap > 0:
				subSet = [item]
				ret.append(subSet)#[item])
				index = cnt
				break
			cnt += 1		
		newLists = []
		if subSet != None and index < len(newList)-1:
			newLists = dpAdvisorHelper(subSet, newList[index+1:], newMaxWork,subjects)
		"""
		for element in newLists:
			#if not element in ret: #?
			ret.append(element)
		"""
		for element in ret:
			newLists.append(element)
		subSet = prev
		subSetWork = subjects[subSet[0]][WORK]
		subSetValue = subjects[subSet[0]][VALUE]
		resizeSet = []
		diff = newMaxWork - subSetWork
		if diff >= 0:
			#start_time = time.time()
			for item in newLists:#ret:
				newCombs = subSet[:]
				tempWork = res[tuple(sorted(item))][WORK]
				if tempWork < newMaxWork:
					totalWork = tempWork + subSetWork
					if totalWork <= newMaxWork:
						for items in item:
							newCombs.append(items)
						if totalWork < newMaxWork:
							resizeSet.append(newCombs)
						tempValue = res[tuple(sorted(item))][VALUE]
						totalValue = tempValue + subSetValue
						newComb = tuple(sorted(newCombs))
						res[newComb] = tuple([totalValue,totalWork])
			for allItems in resizeSet:
				newLists.append(allItems)
			ret = newLists
			#print 'ret ', ret
			#end_time =  time.time()
			#diff = end_time - start_time
			#print 'Time ', diff , 
	elif len(newList) == 1:
		subject = newList[VALUE]
		subjectValue = subjects[subject][VALUE]
		subjectWork = subjects[subject][WORK]
		if subjectWork <= newMaxWork:
			res[tuple([subject])] = tuple([subjectValue,subjectWork])		
			if subjectWork < newMaxWork:
				ret.append([subject])
				subSetValue = subjects[subSet[VALUE]][VALUE]
				subSetWork = subjects[subSet[VALUE]][WORK]
				if subSetWork <= newMaxWork:
					res[tuple(subSet)] =tuple([subSetValue,subSetWork])
					if subSetWork < newMaxWork:
						totalWork  = subjectWork + subSetWork
						difference = newMaxWork - totalWork
						if difference >= 0:
							totalValue = subjectValue + subSetValue
							tempSubSet = subSet[:]
							tempSubSet.append(subject)
							posAns = tuple(sorted(tempSubSet))
							res[posAns] = tuple([totalValue, totalWork])
							if difference > 0:
								ret.append(tempSubSet)
	#print 'len(ret) ', len(ret)
	#print 'len(newList ', len(newList)
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
#smallCatalog = {'6.00': (16, 8), '1.00':(7,7),'6.01':(5,3),'15.01':(9,6)}
smallCatalog = {'6.00': (16, 8), '1.00':(7,7),'6.01':(5,3),'15.01':(9,6), '9.00':(10,2)}
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
for i in range(1,11):#(10,15):#15):#7):#20):#(31):#16):#(10):#(6):#(15)
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
