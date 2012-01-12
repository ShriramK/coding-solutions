def generate_permutations(chars = 4) :
#modify if in need!
	allowed_chars = [    'a',		'b',		'c',		'd',		'e'    ]
	status = []
	for tmp in range(chars) :
		status.append(0)

	last_char = len(allowed_chars)

	rows = []
	for x in xrange(last_char ** chars) :
		rows.append("")
		for y in range(chars - 1 , -1, -1) :
			key = status[y]
			rows[x] = allowed_chars[key] + rows[x]
		#print 'rows[x] ', rows[x]
		for pos in range(chars - 1, -1, -1) :
			if(status[pos] == last_char - 1) :
				status[pos] = 0
			else :
				status[pos] += 1
				break;
	return rows

import sys

list =[]
for i in range(3):
	print len(generate_permutations(i))
	list += generate_permutations(i)
	print list
#print generate_permutations()