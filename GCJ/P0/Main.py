def spkint():
	inputFile = open('A-small-practice.in', 'r')
	#outputFile = open('A-small-practice.out', 'w')
	outputFile = open('A-small-practice2.out', 'w')
	size = inputFile.readline()
	#li = ['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']
	liA = ['y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t',
'h','a','q']
	val = 0
	addNum = ord('a')
	for line in inputFile:
		outputFile.write("Case #%s: " % (val+1))
		for ch in line:
			if ch.isalpha():#check encoding
				outputFile.write(chr(liA.index(ch)+ addNum))
				#outputFile.write(li[ord(ch)-ord('a')])
			elif ch == ' ':
				outputFile.write(ch)
		outputFile.write('\n')#could it be outputFile.write()
		val += 1
	outputFile.close()
	
if __name__ == '__main__':
	spkint()