n,m = map(int,input().split())
a = [list(list(input())) for i in range(n)]
b = [list(list(input())) for i in range(n)]
cout = 0

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            cout += 1
print(cout)