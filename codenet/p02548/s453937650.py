N = int(input())

A = 0

cn = 0

for i in range(1, N+1):
    if N % i != 0:
        B = N // i
    else:
        B = (N // i) - 1
    cn = cn + B

    
print(cn)