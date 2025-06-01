from collections import deque
import operator
from functools import reduce

N,M=map(int,reduce(lambda x,y:x+" "+y,input().split(),"").split())
qs=list(map(lambda _:deque(),range(N)))
lens=list(map(lambda _:0,range(N)))

def min_index(lst):
    return reduce(lambda i,j:i if lst[i]<lst[j] else j, range(len(lst)))

for _ in range(M):
    info,num=map(int,reduce(lambda x,y:str(x)+" "+str(y),input().split()))
    if info==0:
        print(qs[num-1].popleft())
        lens[num-1]-=1
    else:
        idx=min_index(lens)
        qs[idx].append(num)
        lens[idx]+=1