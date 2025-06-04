S = input()
T = input()
len0 = len(S)
S = S * ((len(T) + len(S) - 1) // len(S) * 2)
MOD = 2 ** 31 + 7
base = 26
hashS = [0]
for s in S:
    hashS.append((hashS[-1] * base + ord(s) - 97) % MOD)
hashT = 0
for t in T:
    hashT = (hashT * base + ord(t) - 97) % MOD
ok = [False] * len0
for i in range(len0):
    if (hashS[i+len(T)] - hashS[i] * pow(base, len(T), MOD)) % MOD == hashT:
        ok[i] = True
ret = 0
visited = [-1] * len0
i = 0
while i < len0:
    if ok[i] and visited[i] == -1:
        j = i
        count = 0
        while ok[j]:
            if visited[j] != -1:
                count += visited[j]
                break
            count += 1
            visited[j] = 1
            j = (j + len(T)) % len0
            if j == i:
                print(-1)
                exit()
        visited[i] = count
        if count > ret:
            ret = count
    i += 1
print(ret)