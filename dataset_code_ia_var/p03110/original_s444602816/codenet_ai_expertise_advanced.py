from sys import stdin
from functools import reduce

def to_jpy(amount, currency):
    return int(amount) if currency == "JPY" else float(amount) * 380_000.0

N = int(stdin.readline())
Y = sum(
    to_jpy(*line.split())
    for line in (stdin.readline() for _ in range(N))
)
print(Y)