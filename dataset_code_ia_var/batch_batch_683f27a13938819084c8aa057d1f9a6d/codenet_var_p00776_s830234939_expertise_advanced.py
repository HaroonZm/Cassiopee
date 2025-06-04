import sys
from collections import deque

ALPHABET = [chr(ord('a') + i) for i in range(26)] + ['}']

def unique(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]

def check(a: str, s: str, x):
    n = len(a)
    a_lst = list(a)
    for i in range(1, len(x)):
        idx = x[i]
        if idx > 0:
            for j in range(n):
                if a_lst[j] == ALPHABET[idx]:
                    a_lst[j] = ALPHABET[idx - 1]
                    break
    return ''.join(a_lst) == s[:n]

def foo(s, x, a, n, ans):
    if n == len(a):
        if check(a, s, x):
            ans.add(a)
        return
    sz = len(a)
    if sz < len(s):
        t = a + s[sz]
        if check(t, s, x):
            foo(s, x, t, n, ans)
        next_idx = x[sz] + 1
        if next_idx < 26:
            t2 = a + ALPHABET[next_idx]
            if check(t2, s, x):
                foo(s, x, t2, n, ans)

def main():
    for line in sys.stdin:
        s = line.strip()
        if s == "#":
            break
        n = len(s)
        x = [ALPHABET.index(ch) for ch in s]
        ans = set()
        foo(s, [0] + x, '', n, ans)
        result = sorted(ans)
        count = len(result)
        print(count)
        if count <= 10:
            print('\n'.join(result))
        else:
            print('\n'.join(result[:5]))
            print('\n'.join(result[-5:]))

if __name__ == "__main__":
    main()