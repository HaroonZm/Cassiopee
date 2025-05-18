right = 'yuiophjklnm'
while True:
    S = input()
    if S == '#': break
    ans = 0
    for c1,c2 in zip(S,S[1:]):
        h1 = c1 in right
        h2 = c2 in right
        if h1 != h2: ans += 1
    print(ans)