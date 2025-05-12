n = int(input())
a = list(map(int, input().split()))
a.sort()
a_max=max(a)

check = [0]*(a_max+1)

for i in a:
    if check[i] != 0:
        check[i] = 2
        continue
    if check[i] == 0:
        check[i] = 1
        for j in range(1,a_max//i):
            check[(j+1)*i] = 2

print(check.count(1))