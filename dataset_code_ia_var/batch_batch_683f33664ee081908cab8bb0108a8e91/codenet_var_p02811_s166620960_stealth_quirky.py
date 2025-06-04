result = lambda k, x: ["No","Yes"][(k<<9)+(k<<1)>=x]
exec("a,b=map(int,input().split())\nprint(result(a,b))")