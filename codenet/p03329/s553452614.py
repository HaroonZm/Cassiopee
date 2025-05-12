def read_input():
    n = int(input())
    return n

def count_coin(x, op, min_op):
    if x == 0:
        return 0

    if x in min_op.keys():
        return min_op[x]

    min_count = 10000000
    for o in op:
        if x >= o:
            count = 1 + count_coin(x - o, op, min_op)
            if count < min_count:
                min_count = count

    min_op[x] = min_count
    return min_count

def submit():
    n = read_input()

    ops = [1, 6, 9]

    for op in ops[1:]:
        i = 1
        t = op ** i
        while t <= n:
            ops.append(t)
            t *= op

    ops = list(set(ops))
    ops.sort(reverse=True)
    print(count_coin(n, ops, {}))

if __name__ == '__main__':
    submit()