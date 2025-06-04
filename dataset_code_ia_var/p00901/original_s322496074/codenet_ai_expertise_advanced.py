from functools import cache, partial
from operator import mul
from sys import stdin

MOD = 2011

def main():
    lines = iter(stdin.read().split('\n'))
    while True:
        n = int(next(lines))
        if n == 0:
            break
        S = [next(lines) for _ in range(n)]
        w = len(S[0])

        @cache
        def parse(bcur, bright, top, bottom):
            # Fast find base row and first non-dot column
            base = next(((i, j) for i in range(bcur, bright)
                         for j in range(top, bottom + 1)
                         if S[j][i] != '.'), (None, None))[1]
            if base is None:
                return 0

            cur = bcur

            def seek():
                nonlocal cur
                while 0 <= base < n and cur < bright:
                    c = S[base][cur]
                    if c != '.':
                        return c
                    cur += 1
                return None

            def fraction():
                nonlocal cur
                left = cur
                while cur < w and S[base][cur] == '-':
                    cur += 1
                right = cur + 1 if cur < w else cur
                dividend = parse(left, right, top, base - 1)
                divisor = parse(left, right, base + 1, bottom)
                return dividend * pow(divisor, MOD - 2, MOD) % MOD

            def primary():
                nonlocal cur
                c = seek()
                if c == '(':
                    cur += 1
                    v = expr()
                    cur += 1
                    return v
                cur += 1
                return int(c)

            def powexpr():
                nonlocal cur
                v = primary()
                up = (0 < base and cur < bright and S[base - 1][cur] in '0123456789')
                return pow(v, int(S[base - 1][cur]), MOD) if up else v

            def factor():
                nonlocal cur
                c = seek()
                if c == '-':
                    if cur + 1 < w and S[base][cur + 1] == '.':
                        cur += 1
                        return -factor() % MOD
                    return fraction()
                return powexpr()

            def term():
                nonlocal cur
                result = 1
                while True:
                    result = (result * factor()) % MOD
                    if seek() != '*':
                        break
                    cur += 1
                return result

            def expr():
                nonlocal cur
                acc, sign = 0, 1
                while True:
                    v = term()
                    acc = (acc + sign * v) % MOD
                    nxt = seek()
                    if not nxt or nxt not in '+-':
                        break
                    sign = 1 if nxt == '+' else -1
                    cur += 1
                return acc % MOD
            return expr()

        print(parse(0, w, 0, n - 1))

if __name__ == "__main__":
    main()