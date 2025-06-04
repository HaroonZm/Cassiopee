def ops(a,b):
    return [a//2, b + a//2]
def change(x, y):
    y += x//2
    x //= 2
    return x, y
(a, b, k) = tuple(int(e) for e in input().split())
cnt = 0
while cnt < k:
    if cnt & 1:
        a = a + b//2
        b //= 2
    else:
        args = ops(a, b)
        a, b = args[0], args[1]
    cnt += 1
print(str(a) + " " + str(b))