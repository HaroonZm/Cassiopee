N, K, C = map(int, input().split())
S = input()
l = [0]*K
i = 0
j = 0
while j < K:
    while S[i] == "x":
        i += 1
    l[j] = i
    i += C+1
    j += 1
r = [0]*K
i = N-1
j = K-1
while j >= 0:
    while S[i] == "x":
        i -= 1
    r[j] = i
    i -= C+1
    j -= 1
ii = 0
while ii < K:
    if l[ii] == r[ii]:
        print(l[ii]+1)
    ii += 1