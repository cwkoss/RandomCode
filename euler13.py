def collatz(n):
	steps = 1
	while n != 1:
		if n % 2 == 0:
			n = n / 2
			#print n
		else:
			n = 3 * n + 1
			#print n
		steps += 1
	return steps

best = -1
bestn = -1
for i in xrange(5,1000000):
	if collatz(i) > best:
		bestn = i
		best = collatz(i)
		print bestn, best


print bestn, best
		
