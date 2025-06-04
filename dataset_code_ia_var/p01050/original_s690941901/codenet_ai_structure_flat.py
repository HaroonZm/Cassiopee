f = [0]*128
ch0, ch9n, cha, chzn = ord('0'), ord('9')+1, ord('a'), ord('z')+1

S = list(input())
w = len(S)
for s in S:
    f[ord(s)] += 1
n1 = sum(f[ch0:ch9n])
n2 = w-n1
S2 = []
if n1 > 0:
    start = ch0
    end = ch9n
    n = n1
    while True:
        done = False
        for i in range(start, end):
            if f[i] == 0:
                continue
            f[i] -= 1
            S2.append(i)
            n -= 1
            if n <= 0:
                done = True
                break
        if done:
            break
if n2 > 0:
    start = cha
    end = chzn
    n = n2
    while True:
        done = False
        for i in range(start, end):
            if f[i] == 0:
                continue
            f[i] -= 1
            S2.append(i)
            n -= 1
            if n <= 0:
                done = True
                break
        if done:
            break
ans = w
i = 0
while i < w:
    j = i+1
    while j < w and S2[j] == S2[j-1]+1:
        j += 1
    if j-i > 3:
        ans -= j-i-3
    i = j
print(ans)