N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
s = set()
U = []
ans = 0
for a in A:
    if a in s:
        U.append(a)
        if len(U) == 2:
            ans = U[0] * U[1]
            break
        s.remove(a)
    else:
        s.add(a)
print(ans)