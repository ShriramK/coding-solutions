"""
import itertools

subsets = []
subs = ()
hand = {'a':1, 'c':1,'f':1,'i':1,'s':1,'t':1,'x':1}
for i in range (1,len(hand)+1):
    list1 = list( itertools.permutations(hand,i))
    subsets = subsets + list1
for i in range (0,len(subsets)):
    x=''.join(subsets[i])
    subs = subs + (x,)
print subs
"""
#seq = {'a':1, 'c':1,'f':1,'i':1,'s':1,'t':1,'x':1}
#seq = {'a':1, 'c':1,'f':1,'i':1,'s':1,'t':1,'x':1}
seq  = "acfistx"
seq  = "abc"
def powerset(seq):
	if len(seq):
		head = powerset(seq[:-1])
		return head + [item + [seq[-1]] for item in head]
	else:
		return [[]]
print powerset(seq)