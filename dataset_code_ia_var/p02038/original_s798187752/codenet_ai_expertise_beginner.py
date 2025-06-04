import sys

def machine(x, y):
    if x == 'T' and y == 'F':
        return 'F'
    else:
        return 'T'

N = int(input())
Pn = sys.stdin.readline().strip().split()

i = 1
while i < N:
    Pn[i] = machine(Pn[i-1], Pn[i])
    i += 1

print(Pn[N-1])