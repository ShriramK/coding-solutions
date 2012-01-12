def missing(miss,src):
    "Returns the list of items in src not present in miss"
    return "".join(i for i in src if i not in miss)


def permutation_gen(n,l):
    "Generates all the permutations of n items of the l list"
    for i in l:
        if n <=1: yield "".join(i)
        r = "".join(i)
        for j in permutation_gen(n-1,missing("".join(i),l)):  
			yield r+j

word = "AABBCCDDEE"
li = []
for i in range(len(word)+1):
	for comb in permutation_gen(1, word):#"ABCDE"):
		#if not comb in li:
			li.append(comb)
print li