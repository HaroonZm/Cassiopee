n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = input().split()
    b[i] = int(b[i])
for char in 'SHCD':
    for i in range(1, 14):
        flag = 0
        for j in range(n):
            if a[j] == char and b[j] == i:
                flag = 1
                break
        if flag == 0:
            print(char, i)