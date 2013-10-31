def factors(x):
	from math import sqrt
	from math import ceil
	fin = []
	for i in range(2, int(sqrt(x)+1)):
		if (x % i == 0):
			fin.append(i)
			fin.append(x/i)
	return sorted(fin)



def primes(x):
	fin = []
	for i in range(len(factors(x))):
		if(len(factors(factors(x)[i])) == 0):
			fin.append(factors(x)[i])
	return fin


print primes(600851475143)
