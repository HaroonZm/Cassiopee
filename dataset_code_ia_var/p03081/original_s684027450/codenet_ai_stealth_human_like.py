N, Q = map(int, input().split())
S = input()
TD = []
for i in range(Q):
    temp = input().split()
    TD.append((temp[0], temp[1]))

def isDead(idx):
    cur = idx
    for t, d in TD:
        if S[cur] == t:
            if d == 'L':
                cur -= 1
                if cur < 0:
                    return -1
            else:
                cur += 1
                if cur >= N:
                    return 1 # survived right
    return 0

lft = -1
rgt = N

# for left boundary... kinda binary search?
while rgt - lft > 1:
    mid = (lft + rgt) // 2
    res = isDead(mid)
    if res == -1:
        lft = mid
    else:
        rgt = mid

leftSave = rgt

ll = -1
rr = N
while rr - ll > 1:
    mid = (ll + rr) // 2
    res = isDead(mid)
    if res == 1:
        rr = mid
    else:
        ll = mid

rightSave = ll

# print("INTERVAL", leftSave, rightSave)
result = (rightSave - leftSave + 1)
print(result)

#for check
#for i in range(N):
#    print(i, isDead(i))