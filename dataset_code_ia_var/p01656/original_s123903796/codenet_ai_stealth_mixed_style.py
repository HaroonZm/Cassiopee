N_Q = input().split()
N = int(N_Q[0])
Q = int(N_Q[1])
rename = list()
i = 0
while i < N:
    raw = input().split()
    tmp = [int(raw[0]), raw[1]]
    rename.append(tmp)
    i += 1

def result(q):
    if q < rename[0][0]:
        return 'kogakubu10gokan'
    if q >= rename[-1][0]:
        return rename[-1][1]
    idx = 0
    while idx < N-1:
        if rename[idx][0] <= q and q < rename[idx+1][0]:
            return rename[idx][1]
        idx += 1
    return None

output = result(Q)
print(output)