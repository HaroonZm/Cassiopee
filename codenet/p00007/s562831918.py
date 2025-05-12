n = 10 ** 2
for i in range(int(input())) :
    n = float(n) * 1.05
    if n - int(n) > 0 : n = int(n) + 1
    else : n = int(n)
print(n * (10 ** 3))