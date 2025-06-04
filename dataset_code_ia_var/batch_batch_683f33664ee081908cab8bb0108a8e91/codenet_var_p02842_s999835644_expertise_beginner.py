n = int(input())
found = False
for x in range(n + 1):
    if (x * 108) // 100 == n:
        print(x)
        found = True
        break
if not found:
    print(':(')