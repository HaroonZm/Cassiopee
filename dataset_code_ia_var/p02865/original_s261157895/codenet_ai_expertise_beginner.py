N = int(input())
a = 0
if N % 2 == 0:
    a = int(N / 2) - 1
else:
    a = int(N / 2)
print(a)