q = int(input())
dict = {}
for i in range(q):
    a = input().split()
    if a[0] == "0":
        dict[a[1]] = a[2]
    elif a[0] == "1":
        if a[1] in dict:
            print(dict[a[1]])
        else:
            print(0)
    elif a[0] == "2":
        if a[1] in dict:
            del dict[a[1]]