x = input().split()
x1 = int(x[0])
x2 = int(x[1])
diff = x2 - x1
if diff < 0:
    diff = -diff
print(diff)