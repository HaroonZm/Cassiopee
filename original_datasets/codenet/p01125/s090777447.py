def between(x, y, a):
    lrg = max(x, y)
    sml = min(x, y)
    if (sml <= a <= lrg):
        return True
    else:
        return False

while (True):
    pos = [10, 10]
    result = 'No'
    N = int(input()) # Total number of jewels
    if N == 0:
        break
    jewelPositions = list()
    for i in range(N):
        jewelPos = list(map(int, input().split()))
        jewelPositions.append(jewelPos)

    M = int(input()) # Number of instructions
    # instructions = list()
    for i in range(M):
        # print('==== Currently at ', pos)
        instruction = input().split()
        # print('instruction : ', i)
        if (result == 'Yes'):
            continue
        instruction[1] = int(instruction[1])
        if (instruction[0] == 'E'):
            move = ('x', instruction[1])
        elif (instruction[0] == 'W'):
            move = ('x', -1*instruction[1])
        elif (instruction[0] == 'N'):
            move = ('y', instruction[1])
        elif (instruction[0] == 'S'):
            move = ('y', -1*instruction[1])
        else:
            raise NotImplementedError

        # print('>>>>>>>>>>>>>>> pos: ', pos, ', move: ', move)
        jewelToRemove = []
        for jewel in jewelPositions:

            '''
            if ((move[0] == 'x') and (pos[1] == jewel[1]) and (pos[0] <= jewel[0] <= pos[0]+move[1])) \
                    or ((move[0] == 'y') and (pos[0] == jewel[0]) and (pos[1] <= jewel[1] <= pos[1]+move[1])):
            '''

            if ((move[0] == 'x') and (pos[1] == jewel[1]) and (between(0, move[1], jewel[0]-pos[0]))) \
                    or ((move[0] == 'y') and (pos[0] == jewel[0]) and (between(0, move[1], jewel[1]-pos[1]))):
                # print('---- Collecting a jewel at ', jewel)
                # jewelPositions.remove(jewel)
                jewelToRemove.append(jewel)
            else:
                # print('xxxx Jewel not collected at ', jewel)
                pass

        for jewel in jewelToRemove:
            jewelPositions.remove(jewel)

        if (move[0] == 'x'):
            pos[0] += move[1]
        elif (move[0] == 'y'):
            pos[1] += move[1]

        if not jewelPositions:
            """
            if empty,
            all jewels are collected
            """
            result = 'Yes'
        else:
            pass
        # print('jewels are left at ', jewelPositions)
    print(result)