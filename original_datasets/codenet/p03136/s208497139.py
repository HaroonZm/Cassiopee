N = int(input())

L = list(map(int, input().split()))

max_L = max(L)

L.pop(L.index(max_L))

if sum(L) > max_L:
    print("Yes")
else:
    print("No")