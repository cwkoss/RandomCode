def sumofsquares(n):
	return sum([x ** 2 for x in range(n+1)])

def squareofsums(n):
	return sum(range(n+1))**2

print sumofsquares(10)
print squareofsums(10)
print squareofsums(100) - sumofsquares(100)
