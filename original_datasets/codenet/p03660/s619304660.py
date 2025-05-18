import sys
sys.setrecursionlimit(114514)
N=int(input())
path=[[] for _ in range(N+1)]
for _ in range(N-1):
	a,b=map(int,input().split())
	path[a].append(b)
	path[b].append(a)
fenne=[-1 for _ in range(N+1)]
snuke=[-1 for _ in range(N+1)]
def walk(ar, i, d):
	if ar[i] == -1:
		ar[i] = d
		for x in path[i]:
			walk(ar, x, d+1)
walk(fenne, 1, 0)
walk(snuke, N, 0)
f,s=0,0
for i in range(1, N+1):
	if snuke[i] < fenne[i]:
		s+=1
	else:
		f+=1

print("Fennec" if f > s else "Snuke")