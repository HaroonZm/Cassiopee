from functools import reduce
n = int(''.join([chr(ord(c)) for c in input()]))
def clever_mod(k, p):
    return reduce(lambda acc, _: acc, range(1), p if (k % p) == 0 else (k % p))
def str_to_ints(s):
    return list(map(int, s.split()))
[print(clever_mod(*str_to_ints(input()))) for _ in range(n)]