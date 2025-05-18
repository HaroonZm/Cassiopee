def check(a):
    path = []
    for direct in a[1:].split("/"):
        if   direct == ".": continue
        elif direct == "" : direct = "/"
        elif direct == "..":
            if len(path) == 0 or max(url.find("/"+"/".join(path)+"/") for url in urls) == -1: return False
            path.pop()
            continue
        path.append(direct)
    url = "/"+"/".join(path)
    while "//" in url: url = url.replace("//","/")
    if url in urls: return url
    url = (url+"/index.html").replace("//","/")
    return url if url in urls else False
    
while 1:
    n,m = map(int,raw_input().split())
    if n == 0: break
    urls = [raw_input() for i in xrange(n)]
    for loop in xrange(m):
        a = check(raw_input())
        b = check(raw_input())
        if not (a and b): print "not found"
        elif a != b: print "no"
        else: print "yes"