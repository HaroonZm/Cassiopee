from sys import stdin

def judge(i):
    return "FizzBuzz" if i % 15 == 0 else "Buzz" if i % 5 == 0 else "Fizz" if i % 3 == 0 else str(i)

for line in stdin:
    m, n = map(int, line.split())
    if m == n == 0:
        break
    L = list(range(1, m + 1))
    j = 0
    for _ in range(n):
        c = next(stdin).rstrip()
        if len(L) > 1:
            if judge(j + 1) != c:
                L.pop(j)
                j %= len(L)
            else:
                j = (j + 1) % len(L)
    print(*L)