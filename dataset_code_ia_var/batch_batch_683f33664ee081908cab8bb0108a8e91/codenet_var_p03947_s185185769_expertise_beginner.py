S = raw_input()
res = 0
if len(S) > 0:
    previous = S[0]
    for i in range(1, len(S)):
        if S[i] != previous:
            res = res + 1
            previous = S[i]
print res