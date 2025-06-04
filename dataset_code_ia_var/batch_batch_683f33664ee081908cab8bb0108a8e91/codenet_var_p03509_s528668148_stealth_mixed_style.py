from functools import reduce
n_p = input().split()
n, p = int(n_p[0]), int(n_p[1])
W = []
B = []
i = 0
while i < n:
    pair = input()
    d = pair.split()
    W.append(int(d[0]))
    B.append(int(d[1]))
    i += 1

R = list(map(lambda t: (100-p)*t[0] + p*t[1], zip(W,B)))
R.sort()
R = R[::-1]

result = -reduce(lambda acc, x: acc + x, B, 0) * p

def F():
    cnt = 0
    idx = 0
    while result < 0:
        globals()['result'] += R[idx]
        cnt += 1
        idx += 1
    return cnt

if __name__ == '__main__':
    print(F())