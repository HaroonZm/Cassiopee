vals = input().split()
def add(x, y): return x + y
result = 0
for v in vals:
    result = add(result, int(v))
print(result)