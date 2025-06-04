import sys
for line in sys.stdin:
    d=line.strip()
    if d=='0':
        break
    d=int(d)
    vals=[float(sys.stdin.readline()) for _ in range(d+3)]
    n=d+3
    x=[i for i in range(n)]
    # Choose d+1 points to determine polynomial coefficients using Lagrange interpolation
    # Test each value as wrong by fitting polynomial through others and checking error
    for i in range(n):
        xs=[x[j] for j in range(n) if j!=i]
        ys=[vals[j] for j in range(n) if j!=i]
        coeff=[0]*(d+1)
        for k in range(d+1):
            # Build k-th coefficient using Lagrange basis derivative
            # But better to solve Vandermonde system to find coefficients
            pass
        # Instead, solve linear system Vandermonde to get coefficients
        import numpy as np
        X=np.vander(xs,d+1,increasing=True)
        y=np.array(ys)
        c=np.linalg.solve(X,y)
        fival=sum(c[j]*x[i]**j for j in range(d+1))
        if abs(fival-vals[i])>1.0:
            print(i)
            break