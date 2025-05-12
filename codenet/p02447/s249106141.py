a = []
for i in range(int(input())):
    a.append(list(map(int,input().split())))
a.sort()
for i,j in a:
    print(i,j)