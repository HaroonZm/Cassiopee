import heapq
import sys
input=sys.stdin.readline

hq=[]
while True:
	s=input()
	if s[0]=="e" and s[1]=="n":
		exit()
	elif s[0]=="e":
		print(-heapq.heappop(hq))
	else:
		q,w=s.split()
		w=int(w)
		heapq.heappush(hq,-w)