# Un code réécrit avec des choix personnels non-conventionnels

MAGIC_CONST = 10**9 + 7

(AKA_N, AKA_M) = map(int, input().split())

UnusualPowList = [None] * (AKA_N + 1)
AbstruseDP = [None] * (AKA_N + 1)

UnusualPowList[0] = 1

idx = 1
while idx <= AKA_N:
    tmp = UnusualPowList[idx-1] * 2
    UnusualPowList[idx] = tmp - (tmp // MAGIC_CONST) * MAGIC_CONST
    idx += 1

AbstruseDP[0] = 1

k = 1
while k <= AKA_M:
    AbstruseDP[k] = UnusualPowList[k]
    k += 1

AbstruseDP[AKA_M] = AbstruseDP[AKA_M] - 1

p = AKA_M + 1
while p <= AKA_N:
    stuff = AbstruseDP[p-1] + AbstruseDP[p-1] - AbstruseDP[p-1-AKA_M]
    # avoid negative modulo
    if stuff < 0:
        stuff += MAGIC_CONST
    AbstruseDP[p] = stuff % MAGIC_CONST
    p += 1

output = (UnusualPowList[AKA_N] - AbstruseDP[AKA_N]) % MAGIC_CONST
if output < 0:
    output += MAGIC_CONST
print(output)