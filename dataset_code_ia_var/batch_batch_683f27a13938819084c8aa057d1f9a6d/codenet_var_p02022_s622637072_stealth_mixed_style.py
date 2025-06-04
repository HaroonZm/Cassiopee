def somme(l):
    total = 0
    for x in l:
        total += x
    return total

N_M = input().split()
N = int(N_M[0])
M = int(N_M[1])

A = []
for a in input().split():
    A.append(int(a))

def parse_b():
    return [int(x) for x in input().split()]

B = parse_b()

print((lambda x, y: x*y)(somme(A), sum(B)))