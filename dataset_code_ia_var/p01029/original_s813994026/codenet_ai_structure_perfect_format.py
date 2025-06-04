V_, E_ = map(int, input().split())
A = input().split()
E = [[] for _ in range(V_)]
Used = [[False] * 26 for _ in range(V_)]

for _ in range(E_):
    s, t = map(int, input().split())
    As = A[s]
    At = A[t]
    if As != "?":
        Used[t][ord(As) - 97] = True
    if At != "?":
        Used[s][ord(At) - 97] = True
    E[s].append(t)
    E[t].append(s)

for i, a in enumerate(A):
    if a == "?":
        for j in range(26):
            if not Used[i][j]:
                A[i] = chr(j + 97)
                for u in E[i]:
                    Used[u][j] = True
                break

print("".join(A))