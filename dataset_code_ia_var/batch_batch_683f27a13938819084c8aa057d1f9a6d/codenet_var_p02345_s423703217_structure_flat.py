import math

n, q = map(int, input().split())
b_size = math.ceil(math.sqrt(n))
b_len = math.ceil(n / b_size)
a = []
i = 0
while i < n:
    a.append(2 ** 31 - 1)
    i += 1
b = []
i = 0
while i < b_len:
    left = b_size * i
    right = b_size * (i + 1)
    b.append(min(a[left:right]))
    i += 1
i = 0
while i < q:
    line = input().split()
    com = int(line[0])
    x = int(line[1])
    y = int(line[2])
    if com == 0:
        a[x] = y
        index = x // b_size
        lft = index * b_size
        rgh = (index + 1) * b_size
        b[index] = min(a[lft:rgh])
    else:
        x_index = x // b_size
        y_index = y // b_size
        x_mod = x % b_size
        y_mod = y % b_size
        target = []
        if x_index == y_index:
            j = x
            while j <= y:
                target.append(a[j])
                j += 1
        else:
            if x_mod == 0:
                target.append(b[x_index])
            else:
                j = x
                end = (x_index + 1) * b_size
                while j < end:
                    target.append(a[j])
                    j += 1
            if y_mod == b_size - 1:
                target.append(b[y_index])
            else:
                j = y_index * b_size
                while j <= y:
                    target.append(a[j])
                    j += 1
            idx = x_index + 1
            idx_end = y_index
            if idx <= idx_end - 1:
                k = idx
                while k <= idx_end - 1:
                    target.append(b[k])
                    k += 1
        res = target[0]
        xi = 1
        while xi < len(target):
            if target[xi] < res:
                res = target[xi]
            xi += 1
        print(res)
    i += 1