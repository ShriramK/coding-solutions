# total time to solve -b,c,d: 2:20

from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def constrainedMatchPair(firstMatch, secondMatch, length):
	dlist = []
	for i in firstMatch:
		for j in secondMatch:
			if i + length + 1 == j:
				print 'exact match', target1[i: j+1]
				dlist.append(i)
	return tuple(dlist)

### the following procedure you will use in Problem 3
def subStringMatchExact(target, key):
	dlist = []
	index = find(target, key)
	temp = 0
	if key == "":
		index = -1
	while index != -1:
		dlist.append(temp + index)
		temp = temp + index + 1
		index = find(target[temp:], key)
	return tuple(dlist)

def subStringMatchOneSub(key, target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0, len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key', key, 'into', key1, ",", key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target, key1)
        match2 = subStringMatchExact(target, key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1, match2, len(key1))
        allAnswers = allAnswers + filtered
        print 'match1', match1
        print 'match2', match2
        print 'possible matches for', key1, key2, 'start at', filtered
    return allAnswers

def subStringMatchExactlyOneSub(target, key):
	dlist = []
	exact = subStringMatchExact(target, key)
	print 'EXACT', exact
	allAnswers = subStringMatchOneSub(key, target)
	print 'ALL', allAnswers
	for j in allAnswers:
		for i in exact:
			con = True
			if str(i) == str(j):
				con = False
				break
		if con:
			dlist.append(j)
	return tuple(dlist)

if __name__ == '__main__':
	# print subStringMatchOneSub(key11, target1)
	# print subStringMatchOneSub(key12, target1)
	print subStringMatchExactlyOneSub(target1, key11)
