import sys

def cnt(cards):
    d = {"A":1,"J":11,"Q":12,"K":13}
    h = [0]*14
    for c in cards:
        h[d[c]]+=1 if c in d else h.__setitem__(int(c),h[int(c)]+1) or 0
    return h

def check(h):
    p=t=f=four=False
    m = next((i for i,v in enumerate(h) if v==1),0)
    for v in h:
        if v==2: p+=1
        elif v==3: t=True
        elif v==4: four=True; break
    s1 = all(h[m+i]==1 for i in range(5))
    s2 = h[1]==1 and all(h[i]==1 for i in (10,11,12,13))
    return four,t,p,s1 or s2

for line in sys.stdin:
    cards=line.strip().split(',')
    h=cnt(cards)
    four,three,pairs,straight=check(h)
    print("four card" if four else
          "full house" if three and pairs==1 else
          "straight" if straight else
          "three card" if three else
          "two pair" if pairs==2 else
          "one pair" if pairs==1 else
          "null")