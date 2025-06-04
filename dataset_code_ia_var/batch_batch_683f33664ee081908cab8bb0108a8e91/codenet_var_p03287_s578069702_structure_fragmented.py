import sys

def printn(x):
    sys.stdout.write(x)

def inn():
    return int(input())

def inl():
    return list(map(int, input().split()))

def inm():
    return map(int, input().split())

def ddprint(x, DBG):
    if DBG:
        print(x)

def read_n_and_m():
    return inm()

def read_list(n):
    return inl()

def init_h():
    return {0: 1}

def init_acc(n):
    return [0] * (n + 1)

def compute_acc_and_h(a, n, m, h, acc):
    for i in range(n):
        update_acc_and_h(a, i, m, h, acc)
    return acc, h

def update_acc_and_h(a, i, m, h, acc):
    acc[i + 1] = x = (acc[i] + a[i]) % m
    update_h(h, x)

def update_h(h, x):
    if x in h:
        h[x] += 1
    else:
        h[x] = 1

def compute_sm(h):
    sm = 0
    for x in h:
        sm += calc_pairs(h[x])
    return sm

def calc_pairs(count):
    return count * (count - 1) // 2

def main():
    DBG = True  # or False
    n, m = read_n_and_m()
    a = read_list(n)
    h = init_h()
    acc = init_acc(n)
    acc, h = compute_acc_and_h(a, n, m, h, acc)
    sm = compute_sm(h)
    print(sm)

main()