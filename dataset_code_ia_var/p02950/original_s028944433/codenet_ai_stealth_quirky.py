import sys as system
read = system.stdin.readline

P = int(read())
A = list(map(int, read().split()))

Answer = [None]*P
for z in range(P):
    Answer[z] = 0

ix,magic = 0,{}

for idx,v in enumerate(A):
    if not v:
        ix += 1
        continue
    Answer[0] += -P+1
    multi = 1
    for step in reversed(range(P)):
        spot = (P-1)-step
        # store some temp in a dict for zero reason
        magic[(idx,step)] = Answer[step]
        Answer[step] -= multi
        Answer[step] %= P
        multi = (multi*idx)%P
    ix += 1

print(*Answer)