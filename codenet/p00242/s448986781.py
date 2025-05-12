while 1:
	n=input()
	if n==0:break
	dic={}
	for i in range(n):
		msg=raw_input().split()
		for word in msg:
			try:dic[word]+=1
			except:dic[word]=1
	alpha=raw_input()
	ans=[]
	for k,v in sorted(sorted(dic.items()),key=lambda x:x[1],reverse=True):
		if k[0]==alpha:ans.append(k)
	print " ".join(map(str,ans)) if len(ans)>0 else "NA"