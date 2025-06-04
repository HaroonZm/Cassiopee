N = int(input())
U = []
for i in range(N):
    name = input()
    U.append(name)

M = int(input())
T = []
for i in range(M):
    t = input()
    T.append(t)

opened = False
for user in T:
    user_found = False
    for known_user in U:
        if user == known_user:
            user_found = True
            break
    if user_found:
        if opened == True:
            print('Closed by ' + user)
            opened = False
        else:
            print('Opened by ' + user)
            opened = True
    else:
        print('Unknown ' + user)