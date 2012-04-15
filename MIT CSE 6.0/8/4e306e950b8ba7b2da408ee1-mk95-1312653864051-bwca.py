# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

#import numpy
import time
import pprint

pp = pprint.pprint

SUBJECT_FILENAME = "subjects.txt"
SMALL = "subjects_sm.txt"
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
    d = {}
    for line in inputFile:
        L = line.rstrip().split(',')
        name = L.pop(0)
        value, work = map(int, L)
        d[name] = (value, work)
    print len(d), 'subjects'
    return d

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


#
# Problem 4: Subject Selection By Dynamic Programming
#

# miscellaneous helper functions for dpAdvisor and dpAdvisorHelper
def to_lists(subjects):
    """
    reduce the dictionary to a tuple of lists
    'names':(values, works) -->> ['name'], [values], [works]
    """
    # is there a better way to do this?
    subjx = subjects.keys()
    vlist = subjects.values()
    tmp = zip(*vlist)
    values, works = zip(*vlist)
    return subjx, values, works

def branch_value(branch, value):
    """
    branch is a list of indices taken
    value is the list of subject values from the dictionary
    """
    total = 0
    for i in branch:
        total += value[i]
    return total

# In lecture 13 the brute force code was converted to a
# Dynamic Program algorithm by addition of memoization steps
# the brute force and DP algorithms both used lists

def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    result = {}
    # turn the dictionary into lists for dpAdvisorHelper
    # is there a better way to do this?
    # this relies on the fact that when the dictionary
    # is turned into three lists the key:value relationship
    # is preserved in the indices of the lists
    subjx, value, work = to_lists(subjects)
    # winners should be the list of indices of the optimal solution
    winners = dpAdvisorHelper(work, value, len(value) - 1, maxWork, {})
    # turn winners into dictionary of name:(v,w)
    for i in winners:
        result[subjx[i]] = (value[i], work[i])
    return result

# this problem is exactly like the knapsack problem
# but this solution needs to keep track of the items taken.
# made my own decision tree to try and figure this out
# this is an adaptation of the findMaxVal function from the lecture
def dpAdvisorHelper(work, value, i, work_avail, memo):
    global numcalls, keyerrors
    numcalls += 1
    # the next two lists will gather up the indices
    dont_take = []
    take = []
##    print 'New function instance i: {} numcalls: {} work: {}'.format(i, numcalls, work_avail)

    # see if it is in the memo
    try:
        return memo[(i, work_avail)]
    except KeyError:
        keyerrors += 1
        pass

    # base case for recursion
    if i == 0:
##        print 'Base case - ',
        if work[i] <= work_avail:
            # in this adaptation we care about (need to preserve)
            # the actual indices that are chosen
            # I could only figure out how to make it work with lists
            # so return a list with one element (the index)
            memo[(i, work_avail)] = [i]
##            print 'returning and taking i({})'.format(i,)
            return [i]
        else:
##            print 'returning and not taking i({})'.format(i,)
            return []

    # going left-first depth-first
    # work_avail doesn't change on dont_takes
##    print 'going down a dont_take branch -->', 
    dont_take.extend(dpAdvisorHelper
                     (work, value, i-1, work_avail, memo))

    # must have gotten to the bottom of a dont_take recursion
    # going up to the previous node to start taking - going right
    if work[i] > work_avail:
##        print 'cant take i({}), returning dont_take'.format(i,) 
        memo[(i, work_avail)] = dont_take
        return dont_take
    else:
        # going right and down, work_avail changes
        # take this one and recurse
##        print 'taking i({}) then going down a take branch -->'.format(i,),
        take.extend([i])
        take.extend(dpAdvisorHelper
                    (work, value, i-1, work_avail - work[i], memo))

    # compare the take and dont_take branches
##    print 'comparing branches, i=', i, '-->',
    if branch_value(take, value) >= branch_value(dont_take, value):
        winners = take
        memo[(i, work_avail)] = take
##        print 'take won',
        # print "******** take branch ***********"
        #pp(take)
        #print "****** memo *********"
        #pp(memo)
    else:
        winners = dont_take
        memo[(i, work_avail)] = dont_take
##        print 'dont_take won',
        #print "******** dont_take branch ***********"
        #pp(dont_take)
        #print "****** memo *********"
        #pp(memo)

    # well it looks like it gets here multiple times
    # i thought this would only happen once in the top
    # top level recursion - so i guess i don't completely
    # understand it yet.  even though it works :)
    # need to figure out where in the decision tree this is
    #print "**** final memo *** returning winners ****"
    #pp(memo)
##    print 'returning winners:', winners
    return winners

def test_dpAdvisor():
    global numcalls, keyerrors
    # the correct answer for the test dictionary
    # {'a':(10,2), 'b':(2,3), 'c':(5,9), 'd':(8,4)}
    # with a work constraint of 15 is keys a, c and d
    # total value = 23 and total work = 15
    start = time.clock()
    winners = dpAdvisor(test, 15)
    interval = (time.clock() - start) * 1000
    print 'test  (  4) dictionary work = 15 numcalls: %6i keyerrors: %6i time: %7.3f mSec' % (numcalls, keyerrors, interval)
    printSubjects(winners)
    numcalls = 0
    keyerrors = 0
    start = time.clock()
    winners = dpAdvisor(subjects_sm, 15)
    interval = (time.clock() - start) * 1000
    print 'small ( 20) dictionary work = 15 numcalls: %6i keyerrors: %6i time: %7.3f mSec' % (numcalls, keyerrors, interval)
    printSubjects(winners)
##    numcalls = 0
##    start = time.clock()
##    winners = dpAdvisor(subjects, 5)
##    interval = (time.clock() - start) * 1000
##    print 'large (320) dictionary work =  5 numcalls: %6i  time: %7.3f mSec' % (numcalls, interval)
##    printSubjects(winners)
    numcalls = 0
    start = time.clock()
    winners = dpAdvisor(subjects, 10)
    interval = (time.clock() - start) * 1000
    print 'large (320) dictionary work = 10 numcalls: %6i  time: %7.3f mSec' % (numcalls, interval)
    printSubjects(winners)
##    numcalls = 0
##    start = time.clock()
##    winners = dpAdvisor(subjects, 15)
##    interval = (time.clock() - start) * 1000
##    print 'large (320) dictionary work = 15 numcalls: %6i  time: %7.3f mSec' % (numcalls, interval)
##    printSubjects(winners)
##    numcalls = 0
##    start = time.clock()
##    winners = dpAdvisor(subjects, 20)
##    interval = (time.clock() - start) * 1000
##    print 'large (320) dictionary work = 20 numcalls: %6i  time: %7.3f mSec' % (numcalls, interval)
##    printSubjects(winners)
##    numcalls = 0
##    start = time.clock()
##    winners = dpAdvisor(subjects, 30)
##    interval = (time.clock() - start) * 1000
##    print 'large (320) dictionary work = 30 numcalls: %6i  time: %7.3f mSec' % (numcalls, interval)
##    printSubjects(winners)
##    numcalls = 0
    start = time.clock()
    winners = dpAdvisor(subjects, 30)#31)#40)
    interval = (time.clock() - start) * 1000
    print 'large (320) dictionary work = 40 numcalls: %6i  time: %7.3f mSec' % (numcalls, interval)
    printSubjects(winners)


##implementation of the matrix dp solution from
##the you tube video http://www.youtube.com/watch?v=EH6h7WA7sDw)
##
##uses two arrays
## - V array: rows are item numbers (0-x),
##            columns are work available in the knapsack,
##            cells contain the total value of that item/work
## - Keep array: rows are item numbers,
##               columns are work available in the knapsack,
##               cells contain zero or one for taken or not taken
##implement theses as dictionaries: keys equal (row, column) tuples
##                                  values equal cell values 
##make them up front with all values equal to zero? or on the fly?
##
##go through the V array left-to-right, top-to-bottom:
##    if the item will fit in the knapsack (work less than work avail):
##        note the item value and
##        subtract its work from the column value (work available)
##        if there is any work left:
##            find the cell tha corresponds to:
##                the row above this items row and
##                the column equal to 'work left'
##            add this value to the the item (cells) value
##            compare this value with the cell above the current cell
##            if it is greater:
##                enter the (total) value in this cell
##                enter a one in the corresponding keep cell
##            if it is not greater:
##                enter a the value from the cell above in this cel and
##                enter zero in the corresponding Keep cell
##                
##forget the V array
##start at the bottom right cell - row = max item number, col = max work avail
##recursive posibility here?
##if the cell equals one:
##    'keep' the item
##    subtract the items work from the column (work_avail):
##        look at the cell in the row above and (new) work_avail column
##        repeat
##else if the cell equals zero:
##    look in the row above and repeat

def to_lists1(subjects):
    """
    reduce the dictionary to a tuple of lists
    the lists need to have a dummy zeroith element to work with yutoobAdvisor
    'names':(values, works) -->> ['name'], [values], [works]
    """
    subjx = ['dummy']
    subjx.extend(subjects.keys())

    vlist = subjects.values()
    tmp = zip(*vlist)
    values = ('dummy',) + tmp[0]
    works = ('dummy',) + tmp[1]
    return subjx, values, works

def yutoobAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    result = {}
    # turn the dictionary into lists for dpAdvisorHelper
    # is there a better way to do this?
    # this relies on the fact that when the dictionary
    # is turned into three lists the key:value relationship
    # is preserved in the indices of the lists
    subjx, value, work = to_lists1(subjects)
    # keepArray is the take/don't take results
##    print value
##    print work
    keepArray = makeArrays(value, work, maxWork)
    winners = makewinnerlist(keepArray, work, maxWork)
    # turn winners into dictionary of name:(v,w)
##    print 'winners:', winners
    for i in winners:
        result[subjx[i]] = (value[i], work[i])
    return result

# keep this simple - no recursion, yet
def makeArrays(value, work, maxWork):
    """
    create V-array and Keep-array
    return the Keep-array: a 2d array containing
                           the results of the decision tree
                           {(index, work_avail) : 0 or 1}
    value and work are listsmaxWork is the constraint
    """

    # make a complete array initialized to zero
    # implemented as a dictionary
    # keys are (row, col) tuples of the matrix
    # values are the cell values
    vArray=numpy.zeros((len(value),maxWork+1))
    keepArray=numpy.zeros((len(value),maxWork+1))
#    vArray = dict.fromkeys([(item, workAvail)
#                            for item in range(len(value))
#                            for workAvail in range(1, maxWork + 1)],
#                            0)
#    keepArray = vArray.copy()

    # go through the V array left-to-right, top-to-bottom
    # rows are item/index numbers, cols are the 'room left in the knapsack'
    # the zero row is already made
    for row in range(0, len(value)):
        for col in range(0, maxWork + 1):
            # will this item fit in a knapsack of size col?
            thisitemswork = work[row]
            if thisitemswork < col:
                #print thisitemswork, '<', col
                # there is work left find a previously memoized
                # (item, work) value and include it 
                thisvalue = value[row] + vArray[(row-1, col - thisitemswork)]
            elif thisitemswork == col:
                #print thisitemswork, '==', col
                thisvalue = value[row]
            else:
                #print thisitemswork, '>', col
                # this item won't fit
                thisvalue = vArray[row-1,col]
            # compare thisvalue with the cell value in the row above                
            if thisvalue > vArray[(row-1, col)]:
                # memoize thisvalue
                vArray[(row, col)] = thisvalue
                #print 'took item {0}'.format(thisvalue)
                #print vArray
                # record/memoize(?) that this item is being taken
                keepArray[(row, col)] = 1
            else:
                # bring the previous value forward but
                # don't take the item
                vArray[(row, col)] = vArray[(row-1, col)]
                #print 'didnt take item {0}'.format(vArray[(row-1, col)])
                #print vArray
    # the keepArray and vArray matrices should be populated
    # now need to find the actual indices taken:
    # value optimized and work constrained
##    pp(keepArray)
##    pp\(vArray)
    return keepArray

def makewinnerlist(keepArray, work, maxWork):
##    print work
##    pp\(keepArray)
##    print work
    winners = []
    # start at the bottom-right cell
    row = len(work)-1
    col = maxWork
    while row > 0 and col > 0:
        if keepArray[(row, col)]:
            winners.append(row)
            col -= work[row]
            row -= 1
        else:
            row -= 1
    return winners

def test_yutoobAdvisor():
    global numcalls, keyerrors
    # the correct answer for the utoob dictionary
    # with a work constraint of 5 is
    # {'a':(5,3), 'c':(4,1)}
##    winners = yutoobAdvisor(utoob, 5)
##    print 'utoob dictionary'
##    printSubjects(winners)
    # the correct answer for the test dictionary
    # {'a':(10,2), 'b':(2,3), 'c':(5,9), 'd':(8,4)}
    # with a work constraint of 15 is keys a, c and d
    # total value = 23 and total work = 15
    start = time.clock()
    winners = yutoobAdvisor(subjects_sm, 8)
    interval = (time.clock() - start) * 1000
    print 'small ( 20) dictionary work = 15 time: %7.3f mSec' % (interval)
    printSubjects(winners)
    start = time.clock()
    winners = yutoobAdvisor(subjects, 30)
    interval = (time.clock() - start) * 1000
    print 'small ( 20) dictionary work = 15 time: %7.3f mSec' % (interval)
    printSubjects(winners)
#    start = time.clock()
#    winners = yutoobAdvisor(subjects, 10)
#    interval = (time.clock() - start) * 1000
#    print 'small ( 20) dictionary work = 15 time: %7.3f mSec' % (interval)
#    printSubjects(winners)

def cmp_dpAdvisors():
    print '*************  dpadviser  *************'
    test_dpAdvisor()
    print'************* youtoobAdvisor  *************'
    test_yutoobAdvisor()
    print  '************* test dictionary *************'
    print test
    print '************* small dictionary *************'
    print  subjects_sm

if __name__ == '__main__':
	print 'main!'
	subjects = loadSubjects(SUBJECT_FILENAME)
	test = {'a':(10,2), 'b':(2,3), 'c':(5,9), 'd':(8,4)}
	utoob = {'a':(5,3), 'b':(3,2), 'c':(4,1)}
	subjects_sm = {'2.10': (6, 1), '2.14': (8, 2), '2.11': (9, 3), '2.13': (5, 4), '2.18': (6, 6), '2.15': (9, 4)}
	numcalls = 0
	keyerrors = 0
	#test_yutoobAdvisor()
	test_dpAdvisor()
	"""
	for i in range(1,11):
		dpAdvisor(subjects,i)
	"""