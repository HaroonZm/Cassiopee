def shorten(f):
    if len(f) == 1:
        return f[0]
    g = []
    v = f[0]
    for i in range(1, len(f)):
        s = (v + f[i]) % 10
        g.append(s)
        v = f[i]
    return shorten(g)

while True:
    try:
        s = input().strip()
        nums = []
        for c in s:
            nums.append(int(c))
        result = shorten(nums)
        print(result)
    except EOFError:
        break