from string import *

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'
key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'
target3 = 'abcd'

def subStringMatchExact(target, key):
	dlist = []
	index = find(target, key)
	temp = 0
	while index != -1:
		dlist.append(temp + index)
		temp = temp + index + 1
		index = find(target[temp:], key)
	return tuple(dlist)

"""
def subStringMatchExactRecursive(target, key):
	#dlist = ()
	index = find(target, key)
	temp = 0
	if index != -1:
		dlist = [str(len(target1)-len(target)+temp+index)]
		print 'dlist', dlist
		#temp = index + 1#temp + index + 1
		sSMER = subStringMatchExactRecursive(target[index+1:], key)
		#print 'sSMER', sSMER
		#print 'type(sSMER)', type(sSMER)
		#print 'type(dlist)', type(dlist)
		dlist += sSMER#subStringMatchExactRecursive(target[index+1:], key)
	else:
		dlist = []
	return tuple(dlist)
"""

def subStringMatchExactRecursive(target, key):
	index = find(target, key)
	if index != -1:
		dlist = [len(target1) - len(target)+index]
		dlist += subStringMatchExactRecursive(target[index + 1:], key)
		print 'dlist', dlist
	else:
		dlist = []
	return tuple(dlist)
	
"""
def subStringMatchExactRecursive(target, key):
	#dlist = ()
	index = find(target, key)
	temp = 0
	if index != -1:
		dlist = (len(target1)-len(target)+temp+index,)
		print 'dlist', dlist
		#temp = index + 1#temp + index + 1
		sSMER = subStringMatchExactRecursive(target[index+1:], key)
		#print 'sSMER', sSMER
		#print 'type(sSMER)', type(sSMER)
		#print 'type(dlist)', type(dlist)
		dlist += sSMER#subStringMatchExactRecursive(target[index+1:], key)
	else:
		dlist = tuple()
	return dlist
def subStringMatchExactRecursive(target, key):
	index = find(target, key)
	if index != -1:
		dlist = (len(target1)-len(target)+index,) + subStringMatchExactRecursive(target[index+1:], key)
	else:
		dlist = tuple()
	return dlist
"""

if __name__ == '__main__':
	print 'iterative',subStringMatchExact(target1, key10)
	# print 'recursive',subStringMatchExactRecursive(target1, key10)
	# print 'recursive',subStringMatchExactRecursive(target3, key10)
	print subStringMatchExactRecursive('abcd','e')
