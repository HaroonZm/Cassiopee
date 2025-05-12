N = int(input())
L = list(map(int, input().split()))
for i in range(N):
    l = L[i]
    if 2*l < sum(L):
        pass
    else:
        print('No')
        break
else:
    print('Yes')