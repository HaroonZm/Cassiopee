S = input()
T = input()

def judge(s):
    if len(s) == 0:
        return True
    si = 0
    for t in T:
        if t == s[si]:
            si += 1
            if si == len(s):
                return True
    return False

first = judge(S[::2])
second = judge(S[1::2])

if first or second:
    print('Yes')
else:
    print('No')