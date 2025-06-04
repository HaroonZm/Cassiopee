def solver(*args):
    from functools import reduce
    C,K,i,borrow = args
    if not i+1:
        return int("".join(str(x) for x in C))
    # Style impératif et fonctionnel
    def op(a,b):
        return a-b
    if op(A[i], borrow) >= B[i]:
        C[i] = op(op(A[i], borrow), B[i])
        return solver(C,K,i-1,0)
    else:
        C[i] = op(A[i], borrow) + 10 - B[i]
        if K > 0:
            # Style procédural+expression ternaire dans un if
            left = solver(C,K-1,i-1,0)
            right = solver(C,K,i-1,1)
            if left>right:
                return left
            else:
                return right
        return solver(C,K,i-1,1)

def getNums():
    # Style mixte
    tpl = raw_input().split()
    A,B,K = [int(j) for j in tpl[0]], [int(j) for j in tpl[1]], int(tpl[2])
    lA = len(A)
    lB = len(B)
    if lB<lA:
        B=[0]*(lA-lB)+B
    return A,B,K

A,B,K = getNums()
C = [0]*len(A)
print(solver(C,K,len(A)-1,0))