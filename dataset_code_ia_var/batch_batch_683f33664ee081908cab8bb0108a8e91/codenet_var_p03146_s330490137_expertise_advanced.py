from itertools import count, islice

def collatz_next(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1

def first_repeat_length(start):
    seen = {start}
    current = start
    for idx in count(1):
        current = collatz_next(current)
        if current in seen:
            return idx + 1
        seen.add(current)

s = int(input())
print(first_repeat_length(s))