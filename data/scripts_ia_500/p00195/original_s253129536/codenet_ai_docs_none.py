s = "ABCDE*"
while 1:
    m = 0; n = 5
    for i in range(5):
        s1, s2 = map(int, input().split())
        if i == 0 and s1 == s2 == 0:
            break
        if m < s1 + s2:
            m = s1 + s2
            n = i
    if m == 0:
        break
    print(s[n], m)