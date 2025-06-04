input()
s = input()
cs = s.split("+")
ns = []
ds = []
for c in cs:
    cont = False
    i = 0
    for a in ds:
        if a == c:
            cont = True
            ns[i] += 1
            break
        i += 1
    if not cont:
        ds.append(c)
        ns.append(1)
nums = [0 for _ in range(9)]
for n in ns:
    nums[n - 1] += 1
res = 0
res += 2 * nums[0]
for i in range(1, 9):
    if nums[i] >= 3:
        res += 2 * nums[i] + 4
    else:
        res += 4 * nums[i]
res -= 1
print(res)