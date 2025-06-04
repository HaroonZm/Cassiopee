N = int(input())
D = {True: 'S', False: 'W'}
E = {'o': True, 'x': False}
S = list(input())
for i in range(N):
    S[i] = E[S[i]]
L = {(True, True), (True, False), (False, True), (False, False)}
for a, b in L:
    ans = [None]*N
    ans[0], ans[1] = a, b
    for i in range(1, N-1):
        if not ans[i] ^ S[i]:
            ans[i+1] = ans[i-1]
        else:
            ans[i+1] = not ans[i-1]
    if ans[-1] ^ S[-1] == ans[-2] ^ ans[0] and ans[0] ^ S[0] == ans[-1] ^ ans[1]:
        for i in range(N):
            ans[i] = D[ans[i]]
        print(''.join(ans))
        exit()
print(-1)