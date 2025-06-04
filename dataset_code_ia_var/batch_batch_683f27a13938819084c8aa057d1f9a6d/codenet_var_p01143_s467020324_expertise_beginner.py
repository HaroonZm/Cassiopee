f = open(0)
lines = f.readlines()
ans = []
i = 0
while True:
    NMP = lines[i].split()
    N = int(NMP[0])
    M = int(NMP[1])
    P = int(NMP[2])
    i += 1
    if N == 0:
        break
    X = []
    for j in range(N):
        X.append(int(lines[i]))
        i += 1
    total = sum(X)
    t = X[M-1]
    if t == 0:
        ans.append("0\n")
        continue
    result = int(total * (100 - P) / t)
    ans.append(str(result) + "\n")
open(1, "w").writelines(ans)