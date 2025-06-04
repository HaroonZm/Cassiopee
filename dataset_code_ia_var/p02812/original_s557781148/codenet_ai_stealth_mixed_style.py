def count_abc_occurrences(n, s):
    result = 0
    idx = 0
    while idx < n - 2:
        triple = s[idx:idx+3]
        if triple == 'ABC':
            result = result + 1
        idx += 1
    return result

N = int(input())
S = input()
from functools import reduce
output = (lambda z: reduce(lambda x, y: x + y, [1 if S[i:i+3] == 'ABC' else 0 for i in range(N-2)], 0))(range(N-2)) if N > 2 else 0

if N < 10:
    print(count_abc_occurrences(N, S))
else:
    print(output)