import json
def q1a():
    with open('trunc_log.json', 'r') as f:
        line = f.readline()
        j = json.loads(line)
        print j['time'] - int(j['timestamp'], 16)

print q1a()
    
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

