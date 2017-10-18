from string import *

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'
key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def countSubStringMatch(target, key):
	cnt = 0
	index = find(target, key)
	while index != -1:
		index = find(target, key, index)
		cnt += 1
	return cnt
	
def countSubStringMatchRecursive(target, key):
	cnt = 0
	index = find(target, key)
	if index != -1:  # and index + 1 <= len(target) ):
		target = target[index + 1:]
		cnt = 1 + countSubStringMatchRecursive(target, key)
	return cnt


if __name__ == '__main__':
	# print countSubStringMatchRecursive("aaaa", "a")
	print countSubStringMatchRecursive(target1, key13)
	print countSubStringMatchRecursive(target2, key13)
