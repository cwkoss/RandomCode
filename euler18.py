import json

def main():
    with open('euler67tri', 'r') as f: 
        mxtot = -1
        last = -1 
        for line in f:  
            next = line[:-1].split(' ')            
            if last == -1:
                last = next
            else:
                for i in xrange(len(next)):
                    if i == 0:
                        next[i] = int(next[i]) + int(last[i])
                    elif i == len(last):
                        next[i] = int(next[i]) + int(last[-1])
                    else:
                        next[i] = int(next[i]) + int(max(last[i - 1], last[i]))
                mxtot = max(next)
                print next
                print " "
                last = next
    print "Max is " + str(mxtot)

main()
