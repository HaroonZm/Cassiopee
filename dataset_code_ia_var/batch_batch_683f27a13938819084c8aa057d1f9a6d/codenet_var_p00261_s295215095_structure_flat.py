t = [[1,2],[-1,3],[1,-1],[4,5],[5,2],[2,1]]
while 1:
    s = raw_input()
    if s == '#':
        break
    q = 0
    i = 0
    while i < len(s):
        if q == -1:
            break
        q = t[q][int(s[i])]
        i += 1
    if q == 5:
        print "Yes"
    else:
        print "No"