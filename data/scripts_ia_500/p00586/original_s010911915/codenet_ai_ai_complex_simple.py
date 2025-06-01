from functools import reduce
import operator
import sys

def obfus_sum():
    def int_filter(s):
        return reduce(lambda acc, x: acc*10 + (ord(x)-48), filter(lambda c: c in "0123456789", s), 0)
    for line in iter(sys.stdin.readline, ''):
        try:
            numbers = list(map(int, __import__('re').findall(r'-?\d+', line)))
            if len(numbers) < 2:
                continue
            encoded = list(map(lambda f, n: f(chr(n%256)), [lambda x: x, lambda x: x], numbers))
            s = reduce(operator.add, numbers[:2])
            print(s)
        except Exception:
            break

obfus_sum()