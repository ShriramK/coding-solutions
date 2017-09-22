def compute_thousandth_prime():
	cnt = 1 # for prime #2
	thousandth_prime_num = 3
	while cnt < 1000:
		# print "Value of cnt "+ str(cnt)
		for i in range(thousandth_prime_num / 2):
			# print i
			if thousandth_prime_num % (i+2) != 0:
				if i + 1 == thousandth_prime_num / 2:
					cnt += 1
					i = thousandth_prime_num + 1
					print "thousandth_prime_num " + str(thousandth_prime_num)
			else:
				# print "Entered else loop"
				# i = thousandth_prime_num + 1
				break # print " Value of i " + str(i)
		thousandth_prime_num += 1
	# print "1000th prime number is " + str(thousandth_prime_num)
	# print cnt

if __name__ == '__main__':
	compute_thousandth_prime()
