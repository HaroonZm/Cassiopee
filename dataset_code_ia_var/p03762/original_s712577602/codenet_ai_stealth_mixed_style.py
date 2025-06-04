from sys import stdin

def get_input():
    line = stdin.readline()
    return [int(i) for i in line.split()]

def sumof2(count, arr):
    acc = 0
    for idx, val in enumerate(arr):
        temp = (2*(idx+1)-count-1)*val
        acc = (acc + temp) % (10**9+7)
    return acc

parse = lambda: list(map(int,stdin.readline().split()))
nm = get_input()
n = nm[0]; m = nm[1]        # impératif
X = parse()
def f():
    return [int(z) for z in stdin.readline().split()]
Y = f()
modulo = 1000000007
RES = sumof2(n, X) * sumof2(m, Y)%modulo
print(RES)