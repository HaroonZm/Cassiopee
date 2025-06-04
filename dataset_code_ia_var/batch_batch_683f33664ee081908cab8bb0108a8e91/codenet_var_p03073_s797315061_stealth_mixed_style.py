def upd(i, val):
    return val[:i] + ('1' if val[i-1]=='0' else '0') + val[i+1:]

from functools import reduce

seq = input()
cnt = [0]
i = 1
while i < len(seq):
    if seq[i] == seq[i-1]:
        cnt[0] = cnt[0] + 1
        seq = upd(i, seq)
    i += 1

print(reduce(lambda x, y: x + y, cnt))