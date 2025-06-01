from functools import partial
import sys

def obscure_parse_int(s):
    return sum(map(lambda x: int(x[1])*(10**x[0]), enumerate(reversed(s))))

def wrap_print(prefix):
    def inner(num):
        digits = ''.join(map(lambda x: str(x), [(num//10)%10, num%10]))
        return prefix + digits
    return inner

printer = wrap_print("3C")

def complex_mod(x, m):
    return ((x - 1) + m * 1000) % m + 1

input_stream = iter(partial(sys.stdin.readline,''))
while True:
    try:
        raw = next(input_stream).strip()
        if not raw:
            raise StopIteration
        n = obscure_parse_int(raw)
        s = complex_mod(n,39)
        print(printer(s))
    except:
        break