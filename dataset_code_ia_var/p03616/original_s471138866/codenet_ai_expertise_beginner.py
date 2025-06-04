def calc_ans(x):
    if x < 0:
        return 0
    elif x < X:
        return x
    else:
        return X

if __name__ == '__main__':
    X = int(input())
    K = int(input())
    r = list(map(int, input().split()))
    Q = int(input())

    j = 0
    sign = -1
    s = 0
    e = X
    y = 0
    sand_quantity = []
    sand_quantity.append(r[0])
    i = 1
    while i < K:
        sand_quantity.append(r[i] - r[i-1])
        i += 1

    chasm_time = 0
    i = 0
    while i < Q:
        t_a = input().split()
        t = int(t_a[0])
        a = int(t_a[1])
        while j < K and r[j] < t:
            y = y + sign * sand_quantity[j]
            if y < 0:
                s = s + (-y)
                if e < s:
                    s = e
                y = 0
            if X < y + e - s:
                tmp_diff = (y + e - s) - X
                e = e - tmp_diff
                if e < s:
                    e = s
            if X < y:
                y = X
            chasm_time = r[j]
            j = j + 1
            sign = sign * -1

        tmp_time = t - chasm_time

        if a < s:
            ret = y
        elif a < e:
            ret = y + (a - s)
        else:
            ret = y + (e - s)

        ret = ret + tmp_time * sign

        print(calc_ans(ret))
        i = i + 1