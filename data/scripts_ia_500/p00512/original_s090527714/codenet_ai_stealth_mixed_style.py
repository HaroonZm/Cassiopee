d = {}
n = int(input())
i = 0
while i < n:
    inp = input().split()
    k, v = inp[0], int(inp[1])
    if k in d:
        d[k] += v
    else:
        d[k] = v
    i += 1

def custom_key(x):
    s = 0
    for idx, ch in enumerate(x[::-1]):
        s += 27**idx * (ord(ch) - 64)
    return (s, x)

for key in sorted(d.keys(), key=custom_key):
    print(key, d[key])