def amida():
    line = list(map(int, input().split()))[1:]
    res = [0, 1, 2]
    for i in line:
        if i:
            res[1], res[2] = res[2], res[1]
        else:
            res[0], res[1] = res[1], res[0]
    return res

def func(x, line, flag):
    if line == [0, 1, 2] and flag:
        return True
    for i in range(27):
        if x[i] == 0:
            continue
        swaps = tolist(i)
        x[i] -= 1
        res = func(x, [line[swaps[0]], line[swaps[1]], line[swaps[2]]], True)
        x[i] += 1
        if res:
            return True
    return False

n = int(input())
if n >= 7:
    print("yes")
    exit()
amidas = [amida() for _ in range(n)]
toint = lambda x: x[0] * 9 + x[1] * 3 + x[2]
tolist = lambda x: [x // 9, x % 9 // 3, x % 3]
aa = [0 for _ in range(27)]
for i in amidas:
    aa[toint(i)] += 1

flag = False
for i in range(27):
    if aa[i] == 0:
        continue
    line = [0, 1, 2]
    for j in range(aa[i]):
        swaps = tolist(i)
        line = [line[swaps[0]], line[swaps[1]], line[swaps[2]]]
        if line == [0, 1, 2]:
            flag = True
            break
if flag:
    print("yes")
    exit()
if func(aa, [0, 1, 2], False):
    print("yes")
    exit()
print("no")