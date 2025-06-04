from sys import stdin

age, price = map(int, stdin.readline().split())

print({
    age >= 13: price,
    age > 5: price // 2,
}.get(True, 0))