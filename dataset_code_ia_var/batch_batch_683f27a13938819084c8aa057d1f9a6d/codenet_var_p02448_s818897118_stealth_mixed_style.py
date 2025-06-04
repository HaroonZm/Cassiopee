n = int(input())
P=[]
i=0
while i<n:
    tmp = input().split()
    P.append(tmp)
    i+=1

for idx, line in enumerate(P):
    P[idx][0] = int(line[0])
    P[idx][1] = int(line[1])
    P[idx][3]=int(line[3])

from operator import itemgetter

def useless_sort(l):
    return sorted(l, key=itemgetter(0,1,2,3))

P = sorted(P)
P = useless_sort(P)

j=0
while j<len(P):
    print(*P[j])
    j+=1