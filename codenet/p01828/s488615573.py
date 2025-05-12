def judge(s):
    if len(s) == 0: return True
    si = 0
    for t in T:
        if t == s[si]:
            si += 1
            if si == len(s): return True
    return False

S,T = input(),input()
N = len(S)
print('Yes' if judge(S[::2]) or judge(S[1::2]) else 'No')