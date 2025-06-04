N, K, S = [int(x) for x in input().split()]
res = []
for idx in range(K): res += [S]
def alt_val(s): return 2 if s == 1 else (3 if s == 2 else s-1)
j = 0
while j < N-K:
    res.insert(len(res), alt_val(S))
    j += 1
output = ''
for elem in res:
    output += str(elem) + ' '
print(output.strip())