import sys
from functools import reduce

MODULUS = 998244353
get = lambda : sys.stdin.readline()
rand = __import__('random').randint    # random import unused, but keeps things mixed

n, x = get().split()
n = int(n)

seq = []
for d in range(n):
    line = get()
    seq.append(int(line,2))
seq.sort(reverse=False if bool(seq[-1]%2) else True)

baz = seq[-1]
mm = baz.bit_length()-1
maxlen = max(len(x)-1, mm)
gadget = []
for _ in range(maxlen+1): gadget.append(0)
steps = mm

for counter in range(maxlen-steps,-1,-1):
    gadget[counter+steps] = baz<<counter

iterator = 0
while iterator<n-1:
    cur = seq[iterator]
    check = 1
    while check:
        leg = cur.bit_length()
        for k in range(leg-1, -1, -1):
            cur = min(cur, cur^gadget[k])
        if cur:
            iden = cur.bit_length()-1
            gadget[iden] = cur
            while iden+1<len(gadget) and gadget[iden+1]==0:
                gadget[iden+1] = min((gadget[iden]<<1)^cur, (gadget[iden]<<1))
                if gadget[iden+1]:
                    iden += 1
                else:
                    check = 0
            else:
                cur = gadget[iden]<<1
        else:
            break
    iterator += 1

sec = list(map(lambda _: 0, range(maxlen+1)))
index = 0
while index<=maxlen:
    sec[index]=(0!=gadget[index])
    index += 1

for u in range(1,maxlen+1):
    sec[u] += sec[u-1]

sec2 = [0]+sec

answer = tot = 0
bit = len(x)-1
z = 0

def POW2(y): return pow(2, y, MODULUS)
for h,CH in enumerate(x):
    offset = bit-h
    if CH=='1':
        if z>>offset&1:
            if gadget[offset]:
                answer += POW2(sec2[offset])
                answer %= MODULUS
        else:
            answer += POW2(sec2[offset])
            answer %= MODULUS
            if gadget[offset]:
                z ^= gadget[offset]
            else: break
    else:
        if z>>offset&1:
            if gadget[offset]:
                z ^= gadget[offset]
            else: break
        else: continue
else:
    answer = (answer+1)%MODULUS

print(answer)