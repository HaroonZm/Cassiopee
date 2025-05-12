a = int(input())
b = []

for i in range(a+1):
    if i % 3 == 0 and i % 5 == 0:
      pass
    elif i % 3 == 0:
      pass
    elif i % 5 == 0:
      pass
    else:
      b.append(i)
print(sum(b))