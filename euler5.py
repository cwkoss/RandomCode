def smult(x):
    """
    return the smallest multiple of all numbers less than x
    x of 10 should return 2520
    """
    fin = 1
    ns = range(2, x + 1)
    for i in ns:
        print i
        fin *= i
        j = 2
        while i * j < x:
            ns.remove(i*j)
            print ns
            j += 1
        print ns
    print fin
    
    
    
smult(10)
    
