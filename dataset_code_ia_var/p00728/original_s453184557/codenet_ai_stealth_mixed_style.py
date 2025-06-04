def proc():
    from functools import reduce
    loop=True
    while loop:
        n = int(input())
        if n == 0: loop=False; continue
        idx = 0
        X = []
        while idx < n:
            X.append(int(input()))
            idx+=1
        for i in range(len(X)-1,0,-1):
            if X[i]<X[i-1]:
                X[i],X[i-1]=X[i-1],X[i]
        calc = lambda arr: reduce(lambda a,b:a+b,arr)
        del X[0]; del X[-1]
        print(int(calc(X)/(len(X))))
proc()