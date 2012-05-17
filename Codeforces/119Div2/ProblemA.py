def fun(n, a, b, c)
	ap = n/a
	bp = n/b
	cp = n/c
	max = 0
	tot =0 
	cnt =0
	for i in ap:
		tot += a
		cnt += 1
		for j in bp:
			tot += b
			cnt += 1
			if tot < n:
				pass
			elif tot == n:
				break
				
	for i in ap:
		for j in cp:
			
	for i in bp:
		for j in cp:
			
	for i in ap:
		for j in bp:
			for k in cp:
			

fun()
	n = raw_input()
	a = raw_input()
	b = raw_input()
	c = raw_input()
	print fun(n, a, b, c)