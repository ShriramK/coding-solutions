def translate_googlerese_text():
	input_file = open('A-small-practice.in', 'r')
	# output_file = open('A-small-practice.out', 'w')
	output_file = open('A-small-practice2.out', 'w')
	num_of_lines = input_file.readline()
	# li = ['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w',
	# 'j','p','f','m','a','q']
	list_of_chars = ['y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z']
	list_of_chars.extend(['p','d','r','j','g','t','h','a','q'])
	case_num = 0
	for line in input_file:
		output_file.write("Case #%s: " % (case_num + 1))
		for ch in line:
			if ch.isalpha(): # check encoding
				output_file.write(chr(list_of_chars.index(ch) + ord('a')))
				# output_file.write(list_of_chars[ord(ch) - ord('a')])
			elif ch == ' ':
				output_file.write(ch)
		output_file.write('\n') # could it be output_file.write()
		case_num += 1
	output_file.close()

if __name__ == '__main__':
	translate_googlerese_text()
