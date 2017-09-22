def choose_iter(elements, length):
    new_len = length - 1
    for i in xrange(len(elements)):
        if length == 1:
            yield (elements[i],)
        else:
            for next in choose_iter(elements[i + 1: len(elements)], new_len):
                yield (elements[i],) + next

def choose(l, k):
    return list(choose_iter(l, k))

word ="aabbcd"
li = word
res = []
for i in range(len(word) + 1):
	# res += list(set(choose(li, i)))
	ans = []
	for e in choose(li, i):
		if e not in ans:
			ans.append("".join(e))
	res += ans
	# print list(set(choose(li, i)))
print 'Value of res ', res
