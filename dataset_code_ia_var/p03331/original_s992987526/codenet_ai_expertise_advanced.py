from sys import stdin

def digit_sum(x):
    return sum(map(int, str(x)))

n = int(stdin.readline())

minsum = min(digit_sum(a) + digit_sum(n - a) for a in range(1, n))

print(minsum)