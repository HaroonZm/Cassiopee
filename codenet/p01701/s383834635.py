while 1:
    s = raw_input().replace("north","0").replace("west","1")[::-1]
    if s == "#": break
    u = 90*int(s[0])
    d = len(s)-1
    for i in s[1:]: u = 2*u+(90 if i == "1" else -90)
    while (u+1)%2*d: u /= 2; d -= 1
    print u if d == 0 else "%d/%d"%(u,2**d)