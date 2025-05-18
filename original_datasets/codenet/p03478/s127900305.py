N,A,B = map(int,input().split())
L = []
for i in range(1,N+1) :
    c = 0
    C = list(str(i))
    for j in range(len(C)) :
        c += int(C[j])
    if A <= c <= B :
        L.append(i)
print(sum(L))