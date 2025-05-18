left = "qwertasdfgzxcvb"
while True:
    s = raw_input()
    if s=="#":
        break
    ans = 0
    mode = -1
    for c in s:
        if mode==-1:
            mode = (c not in left)
            continue
        if (mode == 0 and c not in left) or (mode == 1 and c in left):
            mode ^= 1
            ans += 1
    print ans