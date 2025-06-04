m,f,b=map(int,input().split())
need=b-m
print(need if 0<need<=f else '0' if need<=0 else 'NA')