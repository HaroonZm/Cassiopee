n_p = input().split()
N = int(n_p[0])
P = int(n_p[1])

entries = []
for _ in range(N):
    w, b = [int(x) for x in input().split()]
    tt = (w, b)
    entries.append(tt)

def foo(ent, coeff):
    return [((100-coeff)*a+coeff*b) for a,b in ent]

pool = [e[1] for e in entries]
rest = 0
i = 0
for bb in pool:
    rest += P*bb

def bar(ents, coef):
    l = foo(ents, coef)
    l.sort(reverse=True)
    return l

cur = 0
stuff = bar(entries, P)
while True:
    if rest <= 0 or cur >= N:
        break
    rest -= stuff[cur]
    cur += 1

print(cur)