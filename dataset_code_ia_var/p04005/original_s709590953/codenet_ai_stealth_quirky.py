def UnConventional(*argv):
    return list(map(lambda X: int(X), (argv[0].split())))

def main():
    A = UnConventional(input())
    (X, Y, Z) = A
    if pow(X*Y*Z,1,2) == 0: print(0)
    else:
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if A[j]<A[i]:A[i],A[j]=A[j],A[i]
        __import__('builtins').print(A[0]*A[1])
main()