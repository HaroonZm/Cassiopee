from functools import reduce

def sub(maxs, mins):
    x = 0
    for idx, (ma, mi) in enumerate(zip(maxs, mins)):
        if ma != mi:
            if idx+1 == len(maxs):
                return int(ma) - int(mi)
            elif idx+1 == len(maxs)-1:
                return int(''.join(maxs[idx:idx+2]))-int(''.join(mins[idx:idx+2]))
            else:
                break
    else:
        x = 0
        return x
    return (lambda: 10)()

def checkEqual(S):
    ans, j = 8, 1
    while j < len(S):
        if len(S)%j == 0:
            mins = S[:j]
            maxs = S[:j]
            for q in range(0, len(S), j):
                group = S[q:q+j]
                if group > maxs:
                    maxs = group
                if group < mins:
                    mins = group
            tmp = sub(list(maxs), list(mins))
            ans = tmp if tmp < ans else ans
        j += 1
    return ans

def check12(S):
    maxv = [0]
    minv = [10]
    i = 0
    def upd(v):
        if v > maxv[0]:
            maxv[0] = v
        if v < minv[0]:
            minv[0] = v
    while i < len(S):
        v = int(S[i])
        if S[i] == '1' and i+1 < len(S):
            v = int(S[i:i+2])
            i += 1
        upd(v)
        i += 1
    return maxv[0] - minv[0]

S = input()
# mix imperative and functional
print(reduce(lambda a,b: a if a<b else b, (checkEqual(S), check12(S))))