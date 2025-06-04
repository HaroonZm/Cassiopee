from itertools import islice

def judge(s, T):
    it = iter(T)
    return all(c in it for c in s)

S, T = input(), input()
print('Yes' if judge(S[::2], T) or judge(S[1::2], T) else 'No')