#!/usr/bin/env python

def fib(below):
    """
    Return fibonacci as infinite iterator.

    >>> [x for x in fib(10)]
    [1, 1, 2, 3, 5, 8]
    """
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        if a >= below:
            return
        yield a


def strat(below, multiple):
    """
    Sum up all multiples of fibonacci number below a limit.

    >>> strat(1, 2)
    0
    >>> strat(2, 2)
    0
    >>> strat(2, 1)
    2
    >>> strat(10, 2)
    10
    """
    a = 0
    for x in fib(below):
        if x % multiple == 0:
            a += x
    return a

if __name__ == '__main__':
    print strat(4000000, 2)

def strat1(x, mod):
	seq = [1,2]
	while seq[len(seq)-1]+seq[len(seq)-2] <= x:
		seq.append(seq[len(seq)-1]+seq[len(seq)-2])
	return sum([i for i in seq if i % mod == 0])

print strat1(4000000, 2)


