#http://codeforces.com/contest/177/problem/G1
#Fibonacci Numbers
val = raw_input()
li = val.split()

str1 = "a"
str2 = "b"
if int(li[0]) == 1:
	str2 = "a"
elif int(li[0]) == 2:
	str2 = "b"
else:
	cnt = 2 
	while cnt < int(li[0]):
		temp = str2
		str2 += str1
		str1 = temp
		cnt += 1
#print 'str ', str2
val = (1000000007*(10**9+7))
for i in range(int(li[1])):
    testStr = raw_input()
    #print 'testStr ', testStr
    if testStr in str2:
		count = 0
		for j in range(0, len(str2) - len(testStr) + 1):
			if str2[j:len(testStr)+j] == testStr:
				count += 1
				count %= val
		print count % val
    else:
		print 0