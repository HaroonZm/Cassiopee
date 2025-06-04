N = int(input())
lst = [int(x) for x in input().split()]
t = 0
for x in lst:
    t += x

def f(index, acc, result):
    if index >= len(lst) - 1:
        return result
    acc += lst[index]
    diff = abs(t - 2 * acc)
    return f(index + 1, acc, min(result, diff))

if N > 1:
    res = abs(t - 2 * lst[0])
    out = f(1, lst[0], res)
    print(out)
else:
    print(0)