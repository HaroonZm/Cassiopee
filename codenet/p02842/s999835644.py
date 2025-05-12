n = int(input())
for x in range(n+1):
    if x * 108 // 100 == n:
        print(x)
        break
else:
    print(':(')