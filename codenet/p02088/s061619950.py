n = int(input())
arr = [int(x) for x in input().split()]
c0 = 0
c1 = 0
for i in range(n):
        if arr[i] % 2 == 1:
                c1 = c1 + 1
        else:
                c0 = c0 + 1
if c0 == 0 or c1 == 0:
        print(0)
else:
        if c1 % 2 == 0:
                print(n-2)
        else:
                print(n-1)