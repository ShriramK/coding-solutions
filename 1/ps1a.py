def computePrime():
	cnt = 1 #for prime #2
	val = 3
	while cnt < 1000:
		#print "Value of cnt "+ str(cnt)
		for i in range(val/2):
			#print i 
			if val % (i+2) != 0:
				if i+1 == val/2:
					cnt += 1
					i = val+1
					print "val "+ str(val)
			else:
				#print "Entered else loop"
				#i = val+1
				break#print " Value of i " + str(i)
		val += 1
	#print "1000th prime number is " + str(val)
	#print cnt

if __name__ == '__main__':
	computePrime()