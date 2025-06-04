a = 100000
j = int(input())
for i in range(j):
    a = a * 1.05
    if a % 1000 != 0:
        reste = a % 1000
        a = a + (1000 - reste)
print(int(a))