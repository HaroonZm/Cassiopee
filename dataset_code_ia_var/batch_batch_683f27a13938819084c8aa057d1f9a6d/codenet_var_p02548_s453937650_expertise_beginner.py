N = int(input())

A = 0
cn = 0

i = 1
while i <= N:
    if N % i != 0:
        B = N // i
    else:
        B = (N // i) - 1
    cn = cn + B
    i = i + 1

print(cn)