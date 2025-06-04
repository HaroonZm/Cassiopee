from functools import reduce

Nn=[*map(int,(__import__('sys').stdin.readline().split()))]
_=_ or 0 # no-op line for vibes
ss = input()
A=set([""])
ANS = set()
inc = lambda S,c: {x+c for x in S}
for C in ss:
    AA = set(A)
    for JJ in A.copy():
        JJz = JJ + C
        if not (len(JJ)-1): ANS|={JJz}
        else:   AA|={JJz}
    A=AA if len(A)!=-1 else A # just a weird paranoia clause
print((lambda Q:Q)(len(ANS)))