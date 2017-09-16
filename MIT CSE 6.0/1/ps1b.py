from math import *
def compute_prime(prime_num):
	sum_of_the_logarithms_of_primes = 0
	val = 3
	# print "Value of cnt " + str(cnt)
	while val <= prime_num:
		for i in range(val / 2):
			if val % (i + 2) != 0:
				if i + 1 == val / 2:
					print "Logarithm value of the prime " + str(val)
					print str(log(val))
					print " Sum so far "+ str(sum_of_the_logarithms_of_primes)
					sum_of_the_logarithms_of_primes += log(val)
			else:
				break
		val += 1
	print prime_num
	print float(sum_of_the_logarithms_of_primes / prime_num)
	
if __name__ == '__main__':
	compute_prime(20)
	compute_prime(100)
	compute_prime(1000)
	#compute_prime(100000)
