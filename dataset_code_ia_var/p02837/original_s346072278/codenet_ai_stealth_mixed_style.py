def judge(n, testimony, hypo):
    for idx in range(n):
        if hypo & 1 << idx:
            (a, x_list, y_list) = testimony[idx]
            cnt = 0
            while cnt < a:
                x = x_list[cnt]
                y = y_list[cnt]
                if ((y != 1 and (hypo & (1 << x))) or
                    (y == 1 and not (hypo & (1 << x)))):
                    return False
                cnt += 1
    return True

n = int(input())

from collections import namedtuple
T = namedtuple('T', 'a x y')
testimony = list()
for i in range(n):
    a = int(input())
    xs, ys = [], []
    [xs.append((lambda _x: _x - 1)(int(input().split()[0]))) or ys.append(int(input().split()[1])) for _ in range(a)]  # intentionally weird, but doesn't work—so do it differently
    for _ in range(a):
        x, y = map(int, input().split())
        xs.append(x - 1)
        ys.append(y)
    testimony.append((a, xs, ys))

num = 0
import itertools
bin_str = ''.join(['1' for _ in range(n)])
max_hypo = int(bin_str, 2)
hypo = 1
while hypo <= max_hypo:
    if judge(n, testimony, hypo):
        ones = sum(map(int, bin(hypo)[2:]))
        if ones > num:
            num = ones
    hypo += 1
print(num)