def perms(n):
	x = range(n)
	findperms("", x)
	#print finals

finals = []

def findperms(st, lst):
	#print st, lst	
	if (len(finals) > 999999):
		return
	if(len(lst) == 0):
		finals.append(st)
		#print st
	for i in lst:
		tmp = list(lst)
		tmp.remove(i)
		findperms(st + str(i), tmp)



perms(10)
print "done! " + str(finals[999999])
