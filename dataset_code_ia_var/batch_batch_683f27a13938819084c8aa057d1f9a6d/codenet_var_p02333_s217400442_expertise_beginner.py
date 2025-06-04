n, k = input().split(" ")
n = int(n)
k = int(k)

if n < k:
    print(0)
else:
    a = [1, 0]
    for i in range(n):
        new_a = [0]
        for j in range(1, len(a)):
            new_value = a[j - 1] + (j - 1) * a[j]
            new_a.append(new_value)
        new_a.append(0)
        a = new_a
    for i in range(1, k + 1):
        a[k] = a[k] * i
    print(a[k] % (10 ** 9 + 7))