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
    board_id_max = -1
    with open('trunc_log.json', 'r') as f:  
        for line in f:  
            j = json.loads(line)
            board_id_max = max(j['board_id'], board_id_max)
                
    a = [0] * (board_id_max + 1)

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

#print q3()
# result : 00000000005923C3B356E155C7E450A488BBB0C4A6DF187820954E1C35436D61

def q4():
    tot = 0
    with open('trunc_log.json', 'r') as f:  
        for line in f:  
            tot += 1

    sh_per_s = tot/q1b() * 1000
    print "avg shares per ms: " + str(sh_per_s / 1000)
    print "avg shares per s: " + str(sh_per_s)
    # sh_per_s = diff * 2^32 / hashrate
    # hashrate = diff * 2^32 / sh_per_s
    hashrate = 256 * 2 ** 32 / sh_per_s
    print "hashrate is : " + str(hashrate)
    return "Mh/s is : " + str(hashrate / 10 ** 6)
    
#print q4()
"""
result: 
hashrate is : 1224614506.66
Mh/s is : 1224.61450666
"""

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

