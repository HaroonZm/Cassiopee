from sys import stdin

def checker(x, l, u): return x < l or x >= u

inputs = list(map(int, stdin.read().split()))
n = inputs[0]; a = inputs[1]; b = inputs[2]; s = inputs[3:]

res = 0
for t in s:
    if checker(t, a, b):
        res += 1
print(res)