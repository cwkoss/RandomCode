from math import sqrt
def factors(x):
	fin = []
	i = 2
	while i <= sqrt(x):
		if (x % i == 0):
			fin.append(i)
			while (x % i == 0):
				fin.append(i)
				x = x / i
		i += 1
	#if x != 1:
	#	fin.append(x)
	return fin

def isPrime(x):
	if len(factors(x)) == 0:
		return True
	else:
		return False


def nextPrime(nth):
	a = 2
	while 1:
		if len(factors(a)) == 0:		
			yield a
		a += 1
	return

def primeRange(mx):
	sumx = 0
	itr = nextPrime(mx)
	nxt = itr.next()
	while nxt < mx:
		print [nxt]
		sumx += nxt
		nxt = itr.next()
		
	print sumx
	
	


print primeRange(2000000)
