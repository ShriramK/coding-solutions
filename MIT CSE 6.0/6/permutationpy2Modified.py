import sys

list_of_words = []

def generate_permutations(num_of_chars=4):
	# modify if in need!
	allowed_chars = ['a', 'b', 'c', 'd', 'e']
	status = []
	for tmp in range(num_of_chars):
		status.append(0)
	last_char = len(allowed_chars)
	rows = []
	for x in xrange(last_char ** num_of_chars):
		rows.append("")
		for y in range(num_of_chars - 1, -1, -1):
			key = status[y]
			rows[x] = allowed_chars[key] + rows[x]
		# print 'rows[x] ', rows[x]
		for pos in range(num_of_chars - 1, -1, -1):
			if status[pos] == last_char - 1:
				status[pos] = 0
			else:
				status[pos] += 1
				break
	return rows

for i in range(3):
	print len(generate_permutations(i))
	list_of_words += generate_permutations(i)
	print list_of_words
# print generate_permutations()
