n = int(input())
dic = {}
for i in range(n):
    ligne = input().split()
    a = ligne[0]
    b = ligne[1]
    if a == '0':
        c = ligne[2]
        dic[b] = int(c)
    else:
        print(dic[b])