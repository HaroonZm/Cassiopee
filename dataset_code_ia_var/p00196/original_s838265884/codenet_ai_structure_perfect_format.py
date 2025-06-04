def solve():
    N = int(input())
    if N == 0:
        return -1
    score = []
    for i in range(N):
        s = input().split()
        win = 0
        draw = 0
        for j in range(1, len(s)):
            if s[j] == '1':
                continue
            elif s[j] == '0':
                win += 1
            else:
                draw += 1
        score.append((s[0], win, draw))
    res = sorted(score, reverse=True, key=lambda x: (x[1], x[2]))
    for s in res:
        print(s[0])

while True:
    if solve() is not None:
        break