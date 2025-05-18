def judge(ex,torf,i):
	if i==3:
		return eval(ex)
	else:
		return judge(ex,torf+[True],i+1) or judge(ex,torf+[False],i+1)
		
while 1:
	ex=raw_input().split("|")
	if ex[0]=="#":break
	for j in range(len(ex)):
		dic=[]
		ex[j]=list(ex[j])[1:-1]
		for i in range(len(ex[j])):
			if ex[j][i]=="&":ex[j][i]="and"
			elif ex[j][i]=="~":ex[j][i]="not"
			else:
				if ex[j][i] not in dic:
					dic.append(ex[j][i])
					ex[j][i]="torf["+str(len(dic)-1)+"]"
				else:
					ex[j][i]="torf["+str(dic.index(ex[j][i]))+"]"
		ex[j]=" ".join(map(str,ex[j]))
	for clause in ex:
		if judge(clause,[],0):
			print "yes"
			break
	else:
		print "no"