while True:
    n = input()
    if n == 0:
        break
    s = []
    for i in range(n):
        s.append(list(map(int, raw_input().split())))
    r = list(map(int, raw_input().split()))
    flag = 0
    for i in range(len(s)):
        if s[i][1] <= r[0] and s[i][2] <= r[1] and s[i][3] <= r[2] and 4*(s[i][1] + s[i][3]) + 9*s[i][2] <= r[3]:
            print s[i][0]
            flag = 1
    if flag == 0:
        print "NA"