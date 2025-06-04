getdef = lambda: [int(x) for x in input().split()]

sz, mod = getdef()
seq = getdef()

carrysum = [0]
for idx in range(sz):
    carrysum.append((carrysum[-1] + seq[idx]) % mod)

bingo = {}
for j in range(1, sz+1):
    val = carrysum[j]
    if val in bingo:
        bingo[val] += 1
    else:
        bingo[val] = 1

score = 0
for key in bingo:
    v = bingo[key]
    if key == 0:
        score += (v * (v + 1)) // 2
    else:
        score += max(0, ((v - 1) * v) // 2)

print(score)