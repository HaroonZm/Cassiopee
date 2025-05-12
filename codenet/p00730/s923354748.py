while True:
    n,w,h = map(int,input().split())
    if w == 0:
        break
    ls = [[w,h]]
    for i in range(n):
        p,s = map(int,input().split())
        p -= 1
        pw,ph = ls[p]
        if s%(pw+ph) < pw:
            s %= pw+ph
            ls.extend([[min(s,pw-s),ph],[max(s,pw-s),ph]])
        else:
            s = (s-pw)%(ph+pw)
            ls.extend([[pw,min(s,ph-s)],[pw,max(s,ph-s)]])
        ls.pop(p)
    ans = [hi*wi for wi,hi in ls]
    ans.sort()
    print(' '.join(map(str,ans)))