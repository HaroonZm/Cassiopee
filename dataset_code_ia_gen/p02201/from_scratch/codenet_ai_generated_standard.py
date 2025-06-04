n=int(input())
names=[input() for _ in range(n)]
c=names.count("E869120")
print(c if c>0 else 0)