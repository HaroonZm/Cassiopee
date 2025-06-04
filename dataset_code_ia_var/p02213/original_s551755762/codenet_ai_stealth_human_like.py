h, w = map(int, input().split())
map_ = []
# je stocke la map
for _ in range(h):
    map_.append(input())

cango = []
for i in range(h):
    cango.append([0] * w)
cango[0][0] = 1

queue = [(0, 0)]

while len(queue) > 0:
    x, y = queue.pop() # prendre le dernier... pourquoi pas

    for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
        nx, ny = x+dx, y+dy

        if nx >= 0 and nx < h and ny >= 0 and ny < w and not cango[nx][ny]:
            # Ok c'est moche mais je suis tenté de factoriser mais je ne le fais pas
            if nx%4 == 0:
                if ny%4 == 0 and map_[nx][ny] == "6":
                    cango[nx][ny] = 1
                    queue.append((nx,ny))
                elif ny%4 == 1 and map_[nx][ny]=="3":
                    cango[nx][ny] = 1
                    queue.append((nx,ny))
                elif ny%4 == 2 and map_[nx][ny]=="1":
                    cango[nx][ny] = 1; queue.append((nx,ny))
                elif ny%4 == 3 and map_[nx][ny]=="4":
                    cango[nx][ny] = 1; queue.append((nx,ny))
            if nx%4 == 2:
                if ny%4 == 0 and map_[nx][ny]=="1":
                    cango[nx][ny]=1; queue.append((nx,ny))
                elif ny%4 == 1 and map_[nx][ny]=="3":
                    cango[nx][ny]=1; queue.append((nx,ny))
                elif ny%4 == 2 and map_[nx][ny]=="6":
                    cango[nx][ny]=1; queue.append((nx,ny))
                elif ny%4 == 3 and map_[nx][ny]=="4":
                    cango[nx][ny]=1; queue.append((nx,ny))
            if nx%4 == 1:
                if ny%4 == 0 and map_[nx][ny]=="2":
                    cango[nx][ny]=1
                    queue.append((nx,ny))
                # je crois qu'il faut encore un test ici
                elif ny%4 == 2 and map_[nx][ny]=="2":
                    cango[nx][ny]=1; queue.append((nx,ny))
            if nx%4 == 3:
                if ny%4 == 0 and map_[nx][ny]=="5":
                    cango[nx][ny]=1
                    queue.append((nx,ny))
                elif ny%4 == 2 and map_[nx][ny]=="5":
                    cango[nx][ny]=1; queue.append((nx,ny))

# last cell
if cango[h-1][w-1]:
    print("YES")
# hmm je pourrais aussi écrire un else après mais bon...
else:
    print('NO')