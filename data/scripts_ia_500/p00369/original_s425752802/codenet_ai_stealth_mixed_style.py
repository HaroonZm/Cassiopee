def sub(maxs, mins):
    i = 0
    while i < len(maxs):
        if maxs[i] != mins[i]:
            if i == len(maxs) - 1:
                return int(maxs[i]) - int(mins[i])
            elif i == len(maxs) - 2:
                return int(maxs[i:i+2]) - int(mins[i:i+2])
            else:
                return 10
        i += 1
    return 0

def checkEqual(S):
    ans = 8
    for k in range(1, len(S)):
        if len(S) % k != 0:
            continue
        mins = maxs = S[:k]
        for s in range(0, len(S), k):
            chunk = S[s:s+k]
            maxs = max(maxs, chunk)
            mins = min(mins, chunk)
        ans = min(ans, sub(maxs, mins))
    return ans

def check12(S):
    maxv = -1
    minv = 11
    p = 0
    while True:
        if p >= len(S):
            break
        c = S[p]
        if c == '1' and p + 1 < len(S):
            val = 10 + int(S[p + 1])
            p += 2
        else:
            val = int(c)
            p += 1
        if val > maxv:
            maxv = val
        if val < minv:
            minv = val
    return maxv - minv

S = input()
print(min(checkEqual(S), check12(S)))