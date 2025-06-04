from functools import reduce

S = input()

def is_ATGC(ch):
    return ch in ['A', 'G', 'C', 'T']

result = 0
tmp = 0

for idx, ch in enumerate(S):
    if is_ATGC(ch):
        tmp += 1
    else:
        result = tmp if tmp > result else result
        tmp = 0
else:
    result = max(result, tmp)

print((lambda x: x)(result))