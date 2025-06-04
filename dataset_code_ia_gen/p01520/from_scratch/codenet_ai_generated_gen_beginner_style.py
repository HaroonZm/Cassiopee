N,T,E = map(int, input().split())
x = list(map(int, input().split()))

ans = -1
for i in range(N):
    xi = x[i]
    # On vérifie pour k multiples de xi si k est dans l'intervalle [T-E, T+E]
    k = 1
    while xi * k <= T + E:
        if T - E <= xi * k <= T + E:
            ans = i + 1
            break
        k += 1
    if ans != -1:
        break

print(ans)