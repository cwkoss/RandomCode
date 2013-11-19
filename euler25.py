#!/usr/bin/env python

def fib():
    """
    Return fibonacci as infinite iterator.

    >>> [x for x in fib(10)]
    [1, 1, 2, 3, 5, 8]
    """
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a


def fibsize(mx):
    termnum = 1
    for x in fib():
        print termnum, x, len(str(x))
        termnum += 1
        if len(str(x)) >= mx:
            return


fibsize(1000)




