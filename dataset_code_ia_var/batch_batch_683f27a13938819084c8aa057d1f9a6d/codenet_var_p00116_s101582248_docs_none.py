def solve():
    H, W = map(int, input().split())
    if H == 0:
        return False
    MP = [input() for i in range(H)]
    C = [[0]*W for i in range(H)]
    for j in range(W):
        cnt = 0
        for i in range(H-1, -1, -1):
            if MP[i][j] == '.':
                cnt += 1
            else:
                cnt = 0
            C[i][j] = cnt
    ans = 0
    for i in range(H):
        st = [(0, -1)]
        for j in range(W):
            e = C[i][j]
            last = j
            while st and e <= st[-1][0]:
                f, k = st.pop()
                ans = max(ans, (j - k) * f)
                last = k
            st.append((e, last))
        while st:
            f, k = st.pop()
            ans = max(ans, (W - k) * f)
    print(ans)
    return True
while solve():
    ...