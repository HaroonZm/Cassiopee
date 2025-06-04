from collections import defaultdict
def InputInts():
    return [int(e) for e in input().split()]

graph = defaultdict(int)
for row in range(9):
    graph[row,9]=0
    graph[9,row]=0
graph[(9,9)]=0

for i in reversed(range(8)):
    A = (lambda x:8-x)(i)
    B = (-(-(8-i)//2))
    I = i+1
    j=7
    while j>=0:
        if j%2==1:
            J = j+1
            graph[I,J]=graph[I,J+1]+B
        else:
            J = j+1
            graph[I,J]=graph[I,J+1]+A
        j-=1

Q=int(input())
while Q>0:
    Q-=1
    a,b,c,d=InputInts()
    print(
        graph[(a,b)]
        - graph[(c+1,b)]
        - graph[(a,d+1)]
        + graph[(c+1,d+1)]
    )