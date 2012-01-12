from math import *
def computePrime(num):
	sum = 0
	val = 3
	#print "Value of cnt "+ str(cnt)
	while val <= num:
		for i in range(val/2):
			if val % (i+2) != 0:
				if i+1 == val/2:
					print "Logarithm value of the prime " + str(val) + " " + str(log(val)) + " Sum so far "+ str(sum)
					sum += log(val)
			else:
				break
		val += 1
	print num
	print float(sum/num)
	
if __name__ == '__main__':
	computePrime(20)
	computePrime(100)
	computePrime(1000)
	#computePrime(100000)