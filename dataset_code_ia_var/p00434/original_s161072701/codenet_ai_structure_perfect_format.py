n = [i + 1 for i in range(30)]
for i in range(28):
    n.pop(n.index(int(input())))
print(*n, sep='\n')