from math import sqrt
def factors(x):
	fin = [1]
	i = 2
	while i <= sqrt(x):
		if (x % i == 0):
			fin.append(i)
			fin.append(x/i)
		i += 1
	if x != 1:
		fin.append(x)
	return fin



def nextTri():
	a = 1
	sums = 1
	while 1:	
		yield sums
		a += 1
		sums += a

def tryTris(mx):
	itr = nextTri()
	nxt = itr.next()
	while nxt < mx:
		if len(factors(nxt)) > 500:
			print [nxt, len(factors(nxt))]
			break
		print [nxt, len(factors(nxt))]
		nxt = itr.next()
		
	
	

print tryTris(50000000000)
