N = int(input())
L = list(map(lambda x: int(x)-1, input().split()))
res = 0
for idx in range(len(L)):
    res += L[idx]
print(f"{res}")