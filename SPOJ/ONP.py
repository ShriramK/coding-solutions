import sys

def transform( input ):
	output = ""
	li = []
	for i in input:
		if str.isalpha(i):
			output += i
		elif i == '(':
			li.append(i)
		elif i == ')':
			temp = li.pop()
			while temp != '(':
				output += temp
				temp = li.pop()
		else:
			if li[len(li)-1] == '(' or pri(i) < pri(li[len(li)-1]):
				li.append(i)
			else:
				output += li.pop()
				li.append(i)				
	return output

def pri(oprtr):
	val = -1
	if oprtr == '+':
		val = 0
	elif oprtr == '-':
		val = 1
	elif oprtr == '*':
		val = 2
	elif oprtr == '/':
		val = 3
	elif oprtr == '^':
		val = 4
	elif oprtr == '(':
		val = 5
	return val

size = int(raw_input())
for i in range(size):
	print transform(raw_input()) 