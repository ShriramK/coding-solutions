'''http://codeforces.com/contest/177/problem/G1
Fibonacci Numbers
'''

import operator

input_params = raw_input().split()

first_fib_str = "a"
second_fib_str = "b"
fib_string_index = int(operator.getitem(input_params, 0))
if fib_string_index == 1:
	second_fib_str = "a"
elif fib_string_index == 2:
	second_fib_str = "b"
else:
	cnt = 2
	while cnt < fib_string_index:
		temp = second_fib_str
		second_fib_str += first_fib_str
		first_fib_str = temp
		cnt += 1
print 'str ', second_fib_str
val = 1000000007 * (10**9+7)

num_of_queries = int(input_params[1])
for i in range(num_of_queries):
    test_str = raw_input()
    #print 'test_str ', test_str
    first_char = operator.getitem(test_str, 0)
    list_of_pos = []
    for pos in range(len(second_fib_str)):
    	fib_char = operator.getitem(second_fib_str, pos)
        if fib_char == first_char:
            list_of_pos.append(pos)
    if test_str in second_fib_str:
        count = 0
        for j in list_of_pos:		
		# for j in range(0, len(second_fib_str) - len(test_str) + 1):
			# if second_fib_str[j:j + 1] == test_str[:1] and \
			# second_fib_str[j:len(test_str) + j] == test_str:
			if second_fib_str[j : len(test_str) + j] == test_str:
				count += 1
				count %= val
        print count
    else:
		print 0
