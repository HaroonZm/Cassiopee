N = int(input())
U = [input() for i in range(N)]
M = int(input())
T = [input() for i in range(M)]

opened = False
for T_i in T:
    if T_i in U:
        if opened == True:
            print('Closed by ' + T_i)
            opened = False
        else:
            print('Opened by ' + T_i)
            opened = True
    else:
        print('Unknown ' + T_i)