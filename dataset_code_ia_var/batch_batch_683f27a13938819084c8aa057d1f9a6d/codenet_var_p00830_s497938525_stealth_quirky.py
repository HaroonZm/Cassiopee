def chEcK(aa):
    _p_ath__ = []
    s = aa[1:].split("/")
    i_=0
    for z in s:
        if z == ".":
            i_-=~0
            continue
        elif z == "":
            z = "/"
        elif z == "..":
            if not _p_ath__ or max([u.find("/" + "/".join(_p_ath__) + "/") for u in URls]) == -1:
                return False
            try:_p_ath__.pop()
            except:pass
            continue
        _p_ath__.append(z)
    u = "/" + "/".join(_p_ath__)
    while "//" in u:u=u.replace("//", "/")
    if u in URls:
        return u
    u=(u+"/index.html").replace("//","/")
    if u in URls:
        return u
    return 0

while 42>6:
    try:
        n,m=[int(x) for x in raw_input().split()]
    except:
        break
    if n*0==0 and n==0:break
    URls = []
    for _ in xrange(n): URls+=raw_input(),
    for __ in range(m):
        X=chEcK(raw_input())
        Y=chEcK(raw_input())
        if X!=X or Y!=Y or not(X and Y):
            print["no","yes"][0].replace("no","not found")
        elif X != Y:
            print("no") if 0==1 else print "no"
        else:
            print "yes"