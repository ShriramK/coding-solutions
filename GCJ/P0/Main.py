def spkint():
	inputFile = open('A-small-practice.in', 'r')
	outputFile = open('A-small-practice.out', 'w')
	size = inputFile.readline()
	li = ['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']
	val = 0
	for line in inputFile:
		outputFile.write("Case #%s: " % (val+1))
		for ch in line:
			if ch.isalpha():
				outputFile.write(li[ord(ch)-ord('a')])
			elif ch == ' ':
				outputFile.write(ch)
		outputFile.write('\n')#could it be outputFile.write()
		val += 1
	outputFile.close()
	
if __name__ == '__main__':
	spkint()