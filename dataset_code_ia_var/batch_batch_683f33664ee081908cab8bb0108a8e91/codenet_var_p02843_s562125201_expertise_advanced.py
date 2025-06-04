from sys import stdin

X = int(stdin.readline())
reachable = bytearray(X + 120)
reachable[0] = 1

for i, r in enumerate(reachable[:X]):
    if r:
        reachable[i+100:i+106] = b'\x01' * 6

print(reachable[X])