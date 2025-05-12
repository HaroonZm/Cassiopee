import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N,M,*X = map(int,read().split())

MOD = 10 ** 9 + 7

def mult(a,b,c,d,e,f):
    # (a+bx+cx^2)(d+ex+fx^2) modulo 1-4x+2x^2-x^3
    a,b,c,d,e = a*d,a*e+b*d,a*f+b*e+c*d,b*f+c*e,c*f
    b += e; c -= 4*e; d += 2*e; e = 0
    a += d; b -= 4*d; c += 2*d; d = 0
    a %= MOD; b %= MOD; c %= MOD
    return a,b,c

# (1/x)^i modulo (1-4x+2x^2-x^3)
M = 10 ** 5
A1 = [0] * (M+1)
a,b,c = 1,0,0
for i in range(M+1):
    A1[i] = (a,b,c)
    a,b,c = b+4*a,c-2*a,a
    a %= MOD; b %= MOD; c %= MOD

# (1/x)^Mi modulo (1-4x+2x^2-x^3)
A2 = [0] * (M+1)
a,b,c = 1,0,0
d,e,f = A1[M]
for i in range(M+1):
    A2[i] = (a,b,c)
    a,b,c = mult(a,b,c,d,e,f)

def power(n):
    # (1/x)^n modulo (1-4x+2x^2-x^3)
    q,r = divmod(n,M)
    a,b,c = A1[r]
    d,e,f = A2[q]
    return mult(a,b,c,d,e,f)

X.append(N)

a,b,c = 0,1,1
prev_x = 0
for x in X:
    a,b,c = mult(a,b,c,*power(x - prev_x))
    b -= a; c -= a
    prev_x = x

answer = a
print(answer)