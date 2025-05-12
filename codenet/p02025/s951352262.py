def f(): return map(int,input().split())
h,w=f();print(sum([sum([(x+1)*(w-x)*v for x,v in enumerate(f())])*(y+1)*(h-y)for y in range(h)]))