num = int(input())

info = list()
buildings = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

for i in range(num):
    info = input().split()
    buildings[int(info[0])-1][int(info[1])-1][int(info[2])-1] += int(info[3])

for i, b in enumerate(buildings):
    for f in b:
        print(' ', end='')
        print(' '.join(map(str, f)))
    if not i == (len(buildings) - 1):
        print('#'*20)