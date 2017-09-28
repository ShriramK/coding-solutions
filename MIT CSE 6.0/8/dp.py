res = []

def msum(a):
    return max([(sum(a[j : i]), (j, i)) for i in range(1, len(a) + 1) \
               for j in range(i)])
"""
def msum(a):
	for i in range(1, len(a) + 1):
		for j in range(i):
			res(sum(a[j:i]), (j, i)
"""
print msum([1, 2, -5, 4, 7, -2])
# print max(res)
