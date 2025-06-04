from itertools import count

n, k = map(int, input().split())
forbidden_digits = set(input().split())

for candidate in count(n):
    if forbidden_digits.isdisjoint(str(candidate)):
        print(candidate)
        break