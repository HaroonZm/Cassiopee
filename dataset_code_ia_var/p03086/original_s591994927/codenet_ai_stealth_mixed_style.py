S = input()
seq = ['A', 'C', 'G', 'T']
res = 0

def check(s):
    return all(x in seq for x in s)

i = 0
while i < len(S):
    if S[i] not in seq:
        i += 1
        continue
    j = i
    current = ''
    while True:
        try:
            if S[j] in seq:
                current += S[j]
                if len(current) > res:
                    res = len(current)
                j += 1
            else:
                break
        except:
            break
    i += 1

print(res)