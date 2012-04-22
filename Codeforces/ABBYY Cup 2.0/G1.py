#http://codeforces.com/contest/177/problem/G1
import sys
val = raw_input()
li = val.split()

str1 = "a"
str2 = "b"
cnt = 2 
while cnt < int(li[0]):
    temp = str2
    str2 += str1
    str1 = temp
    cnt += 1
print 'str ', str2
for i in range(int(li[1])):
    testStr = raw_input()
    print 'testStr ', testStr
    if testStr in str2:
        print str2.count(testStr)