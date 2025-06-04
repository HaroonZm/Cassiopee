n = int(input())
ab = [1, 0]
def op1(x):
    ab[0] *= x
    ab[1] *= x
def op2(x):
    ab[1] += x
def op3(x):
    ab[1] -= x

ops = {1: op1, 2: op2, 3: op3}

i = 0
while i < n:
    qx = input().split()
    q = int(qx[0])
    x = int(qx[1])
    if q in ops:
        ops[q](x)
    else:
        pass
    i += 1

print((-ab[1], ab[0]))