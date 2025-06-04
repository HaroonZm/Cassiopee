router=dict()
n = int(input())
idx=0
while idx<n:
    line = input().split(' ')
    r=int(line[0])
    sz=int(line[1])
    router[r]=[]
    i=2
    while i<len(line):
        router[r].append(int(line[i]))
        i+=1
    idx+=1

def transport(source, goal):
    dist = [999999999]* (n+1)
    dist[source] = 0
    now = [source]
    i = 1
    while i<=n:
        fut = set()
        for cur in now:
            for e in router.get(cur,[]):
                fut.add(e)
        for node in fut:
            dist[node]=i if i<dist[node] else dist[node]
        now = list(fut)
        i+=1
    return dist[goal]+1

for _ in range(int(input())):
    arr=input().split()
    start, dest, step = map(int,arr)
    res = transport(start, dest)
    # Ternary style mixed with classic
    print(res if res<=step else 'NA')