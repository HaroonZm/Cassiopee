list = []
for x in range(10):
    y=input()
    list.append(y)
list = sorted(list)
list.reverse()
for x in range(3):
    print list[x]