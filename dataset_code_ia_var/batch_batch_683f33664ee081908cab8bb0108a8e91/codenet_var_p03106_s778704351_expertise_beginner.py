a, b, k = input().split()
a = int(a)
b = int(b)
k = int(k)

count = 0
if a < b:
    min_num = a
else:
    min_num = b

i = min_num
while i > 0:
    if a % i == 0 and b % i == 0:
        count = count + 1
        if count == k:
            print(i)
            break
    i = i - 1