#ARC071C
import sys

n=int(input())

alpnum=[]
alpnumtmp=[]
for i in range(0,26):
	alpnum.append(0)
	alpnumtmp.append(0)

tmp = input()
for j in range(0,len(tmp)):
	alpnum[ord(tmp[j])-ord("a")]+=1

for i in range(1,n):
	tmp = input()
	for j in range(0,26):
		alpnumtmp[j]=0
	for j in range(0,len(tmp)):
		alpnumtmp[ord(tmp[j])-ord("a")]+=1
	for j in range(0,26):
		alpnum[j]=min(alpnum[j],alpnumtmp[j])

ans=""
for i in range(0,26):
	for j in range(0,alpnum[i]):
		ans+=chr(97+i)

#print(alpnum)
print(ans)