def f(n): return n*f(n-1) if n!=0 else 1
print f(input())