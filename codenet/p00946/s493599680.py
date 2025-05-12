N,M = map(int,input().split())

lis = [False] * N
end = [False] * N
aft = []
for i in range(M):

    e = int(input())

    aft.append(e)
    lis[e-1] = True

aft.reverse()

for i in aft:

    if not end[i-1]:
        print (i)
        end[i-1] = True

for i in range(N):

    if not lis[i]:
        print (i+1)