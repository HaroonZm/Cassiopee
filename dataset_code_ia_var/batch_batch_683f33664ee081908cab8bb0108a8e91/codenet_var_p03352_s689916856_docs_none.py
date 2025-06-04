import sys, os

f = lambda: list(map(int, input().split()))
if 'local' in os.environ:
    sys.stdin = open('./input.txt', 'r')

def solve():
    x = f()[0]
    a = [0]*10001
    a[1] = 1
    for i in range(2, 1000):
        if i*i <= 1000:
            a[i*i] = 1
            k = 3
            while i**k <= 1000:
                a[i**k] = 1
                k += 1
        else:
            break
    for i in range(x, 0, -1):
        if a[i] == 1:
            print(i)
            break

solve()