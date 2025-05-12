d={}
for _ in[0]*int(input()):
 k,v=input().split()
 d[k]=d.get(k,0)+int(v)
for l,k in sorted([len(x),x]for x in d):
 print(k,d[k])