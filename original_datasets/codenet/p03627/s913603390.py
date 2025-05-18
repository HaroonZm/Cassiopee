N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
s = set()
U = []
ans = 0
for a in A:
    if a in s:
        U.append(a)
        if len(U) >= 2:
            ans = U[0]*U[1]
            break
        s.remove(a)
    else:
        s.add(a)
print(ans)