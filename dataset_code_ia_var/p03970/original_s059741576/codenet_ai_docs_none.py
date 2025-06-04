import sys

S = sys.stdin.readline().strip()
template = 'CODEFESTIVAL2016'
res = 0
i = 0
while i < len(S):
    if S[i] != template[i]:
        res += 1
    i += 1
print res