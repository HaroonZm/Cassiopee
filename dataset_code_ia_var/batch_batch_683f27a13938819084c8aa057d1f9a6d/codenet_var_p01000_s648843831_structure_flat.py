case = 1
while True:
    n = int(input())
    if n == 0:
        break
    if case != 1:
        print()
    exist_mp = [[[0] * 7 for _ in range(7)]]
    for z in range(5):
        mp = [[0] * 7]
        for _ in range(5):
            mp.append([0] + list(map(int, list(input()))) + [0])
        mp.append([0] * 7)
        exist_mp.append(mp)
        if z != 4:
            input()
    exist_mp.append([[0] * 7 for _ in range(7)])

    cnt_mp = [[[0] * 7 for _ in range(7)] for _ in range(7)]
    for z in range(1, 6):
        for y in range(1, 6):
            for x in range(1, 6):
                if exist_mp[z][y][x]:
                    cnt_mp[z][y][x] -= 1
                    for nz in (z - 1, z, z + 1):
                        for ny in (y - 1, y, y + 1):
                            for nx in (x - 1, x, x + 1):
                                cnt_mp[nz][ny][nx] += 1

    s = input()
    if s == "":
        birth_num = set(list(map(int, input().split()))[1:])
        death_num = set(list(map(int, input().split()))[1:])
    else:
        birth_num = set(list(map(int, s.split()))[1:])
        death_num = set(list(map(int, input().split()))[1:])

    birth_list = []
    death_list = []
    limit = n
    while limit > 0:
        birth_list.clear()
        death_list.clear()
        for z in range(1,6):
            for y in range(1,6):
                for x in range(1,6):
                    if not exist_mp[z][y][x] and cnt_mp[z][y][x] in birth_num:
                        birth_list.append((x,y,z))
                    if exist_mp[z][y][x] and cnt_mp[z][y][x] not in death_num:
                        death_list.append((x,y,z))
        for x,y,z in birth_list:
            exist_mp[z][y][x] = 1
            cnt_mp[z][y][x] -= 1
            for nz in (z-1,z,z+1):
                for ny in (y-1,y,y+1):
                    for nx in (x-1,x,x+1):
                        cnt_mp[nz][ny][nx] +=1
        for x,y,z in death_list:
            exist_mp[z][y][x] = 0
            cnt_mp[z][y][x] +=1
            for nz in (z-1,z,z+1):
                for ny in (y-1,y,y+1):
                    for nx in (x-1,x,x+1):
                        cnt_mp[nz][ny][nx] -=1
        limit -= 1

    print("Case {}:".format(case))
    for z in range(1,6):
        for y in range(1,6):
            print(*exist_mp[z][y][1:6],sep="")
        if z != 5:
            print()
    case += 1