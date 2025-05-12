a,b = map(int,input().split(" "))
t = (a - b) * 100 + b * 1900
print(t * (2 ** b))