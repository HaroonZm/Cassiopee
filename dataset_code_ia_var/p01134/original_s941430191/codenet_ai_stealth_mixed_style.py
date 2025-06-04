import math

epsilon = 1e-10

def is_close(a, b): return abs(a-b) < epsilon

eqv = lambda a, b: is_close(a.real, b.real) and is_close(a.imag, b.imag)

def cross(x, y):
    return x.real*y.imag - x.imag*y.real

isects = lambda a1,a2,b1,b2: (cross(a2-a1,b1-a1)*cross(a2-a1,b2-a1)<epsilon) and (cross(b2-b1,a1-b1)*cross(b2-b1,a2-b1)<epsilon)

def intersection(a1,a2,b1,b2):
    veca = a2 - a1
    vecb = b2 - b1
    try:
        return a1 + veca * cross(vecb, b1-a1) / cross(vecb, veca)
    except ZeroDivisionError:
        return None

def main():
    from sys import stdin
    # Read input using input() for compatibility
    while 1:
        N = int(input())
        if not N:
            break
        all_lines = []
        count=0
        while count<N:
            temp=tuple(map(int, input().split()))
            all_lines.append((complex(temp[0], temp[1]), complex(temp[2], temp[3])))
            count+=1
        answer = 2
        c = 1
        while c < N:
            xs = []
            for d in range(c):
                lA, lB = all_lines[c], all_lines[d]
                if isects(lA[0],lA[1],lB[0],lB[1]):
                    pt = intersection(lA[0],lA[1],lB[0],lB[1])
                    if pt and -100+epsilon<=pt.real<=100-epsilon and -100+epsilon<=pt.imag<=100-epsilon:
                        xs.append(pt)
            cc = min(len(xs),1)
            z = 1
            while z < len(xs):
                f = False
                for zz in range(z):
                    if eqv(xs[z], xs[zz]):
                        f = True
                if not f:
                    cc+=1
                z+=1
            answer += cc+1
            c+=1
        print(answer)

main()