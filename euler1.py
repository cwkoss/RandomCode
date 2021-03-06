# If we list all the natural numbers below
# 10 that are multiples of 3 or 5, we get 
# 3, 5, 6, 9. The sum of these multiples is 23
#
# Find the sum of all the multiples of 3 or 5
# below 1000

def strat1(x, y, mx):
	count = 0
	for i in range(mx):
		if (i % x == 0) or (i % y == 0):
			count += i
	return count

def strat2(x,y,mx):
	def f(n): return not n % x * n % y
	return sum(filter(f, range(min(x,y), mx)))

def strat3(x,y,mx):
	return sum([i for i in range(mx) if not i % x * i % y])

print strat1(3,5,1000)
print strat2(3,5,1000)
print strat3(3,5,1000)
