N  = int(input())

data = [list(map(int,input().split())) for _ in range(N)]
team = data[0][2]
player = data[0][1]
t1 = 0
t2 = 0
f1 = 0
f2 = 0
for i in range(1,N):
    if data[i][2] == team:
        if data[i][1] != player:
            if team == 0:
                if t1 < ((data[i][3] - data[i-1][3])**2 + (data[i][4] - data[i-1][4])**2)**(1/2):
                    t1 = ((data[i][3] - data[i-1][3])**2 + (data[i][4] - data[i-1][4])**2)**(1/2)
                    f1 = (data[i][0]- data[i-1][0])/60
                if t1 == ((data[i][3] - data[i-1][3])**2 + (data[i][4] - data[i-1][4])**2)**(1/2):
                    if f1 > (data[i][0]- data[i-1][0])/60:
                        f1 = (data[i][0]- data[i-1][0])/60
            if team == 1:
                if t2 < ((data[i][3] - data[i-1][3])**2 + (data[i][4] - data[i-1][4])**2)**(1/2):
                    t2 = ((data[i][3] - data[i-1][3])**2 + (data[i][4] - data[i-1][4])**2)**(1/2)
                    f2 = (data[i][0] - data[i-1][0])/60
                if t2 == ((data[i][3] - data[i-1][3])**2 + (data[i][4] - data[i-1][4])**2)**(1/2):
                    if f2 > (data[i][0]- data[i-1][0])/60:
                        f2 = (data[i][0]- data[i-1][0])/60
    player = data[i][1]
    team = data[i][2]
if t1 == 0 :
    print(-1,-1)
else:
    print(t1,f1)
if t2 == 0:
    print(-1,-1)
else:
    print(t2,f2)