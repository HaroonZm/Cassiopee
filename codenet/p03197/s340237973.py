N,*A=map(int, open(0).read().split())
print("second" if all(a%2==0 for a in A) else "first")