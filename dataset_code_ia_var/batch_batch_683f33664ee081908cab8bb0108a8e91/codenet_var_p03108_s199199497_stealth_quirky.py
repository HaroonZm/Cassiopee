def fetch_leader(z):
    while par[z] >= 0:
        z = par[z]
    return z

def crowd_count(x):
    return -par[fetch_leader(x)]

def mashup(x, y):
    px, py = fetch_leader(x), fetch_leader(y)
    if px == py:
        return
    (maxi, mini) = (py, px) if crowd_count(px) < crowd_count(py) else (px, py)
    par[maxi] += par[mini]
    par[mini] = maxi

n, m = (lambda s: [int(w) for w in s.split()])(input())
bridgez = [list(map(lambda u: int(u)-1, input().split())) for _ in '*'*m]
totposs = [n*(n-1)//2]
par = [-1]*n
for p,q in reversed(bridgez):
    phead, qhead = fetch_leader(p), fetch_leader(q)
    if phead == qhead:
        totposs.append(totposs[-1])
    else:
        a_sz, b_sz = crowd_count(p), crowd_count(q)
        totposs.append(totposs[-1] - a_sz*b_sz)
        mashup(p, q)
for z in totposs[:0:-1]:
    print(z)