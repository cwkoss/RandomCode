import json
def q1a():
    with open('trunc_log.json', 'r') as f:
        line = f.readline()
        j = json.loads(line)
        return j['time'] - int(j['timestamp'], 16)

#print q1a()

def q1b():
    with open('trunc_log.json', 'r') as f:  
        for line in f:  
            j = json.loads(line)
            fin_time = j['time']
            fin_timestamp = j['timestamp']
    return fin_time - int(fin_timestamp, 16)

#print q1b()

def q1c():
    total = 0 
    with open('trunc_log.json', 'r') as f:  
        for line in f:  
            j = json.loads(line)
            total += j['time'] - int(j['timestamp'], 16)  
    return total

#print q1c()

def q2():
    a = [0,0,0,0]
    with open('trunc_log.json', 'r') as f:  
        for line in f:  
            j = json.loads(line)
            a[j['board_id']] += 1
    return "Index: " + str(a.index(max(a))) + " shares: " + str(max(a))
        
#print q2() 

def q3():
    fin = ''
    with open('trunc_log.json', 'r') as f:
        line = f.readline()
        line = f.readline()
        j = json.loads(line)
        string = j['hash']
    for i in range(8, -1, -1):
        #print i * 8,  (i + 1) * 8
        #print string[i * 8: (i + 1) * 8]
        fin += string[i * 8: (i + 1) * 8]
    return fin

print q3()
# result : 


"""
with open('trunc_log.json', 'r') as f:  
    for line in f:  
        j = json.loads(line)
        #print "board_id: " + str(j['board_id']),
        #print "nonce: " + str(j['nonce']),
        #print "timestamp: " + str(j['timestamp']),
        #print "time: " + str(j['time']),
        #print "leaf_id: " + str(j['leaf_id'])
        #print "hash: " + str(j['hash'])
"""

