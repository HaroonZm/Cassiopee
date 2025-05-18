n = int(input())

minsum = 900000

for i in range(n - 1):
    count = 0
    a = i +1
    b = n -i -1
    for c in str(a):
        count += int(c)
    for c in str(b):
        count += int(c)
    if count < minsum:
        minsum = count
print(minsum)