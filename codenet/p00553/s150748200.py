x = [int(input()) for s in range(5)]
if x[0] > 0:
    print(int(x[4]*(x[1]-x[0])))
else:
    t = abs(x[0])*x[2]+x[3]+x[1]*x[4]
    print(t)