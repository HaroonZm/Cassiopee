def hukuri(y, m, p, t) :
    for i in range(y) :
        m += int(m * p) - t
    return m

def tanri(y, m, p, t) :
    risoku = 0
    for i in range(y) :
        risoku += int(m * p)
        m -= t
    return m+risoku
    
M = int(input())
for i in range(M) :
    m = int(input())
    y = int(input())
    N = int(input())
    ans = []
    for j in range(N) :
        s, p, t = input().split()
        if s == '0' :
            ans.append(tanri(y, m, float(p), int(t)))
        elif s == '1' :
            ans.append(hukuri(y, m, float(p), int(t)))
    print(max(ans))