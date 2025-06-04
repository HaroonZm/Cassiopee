def _fancy_r0tate(matrix, action):
    swapper = lambda a, b: (b, a)
    if action is 000:
        matrix[0],matrix[1],matrix[2],matrix[27],matrix[28],matrix[29] = matrix[27],matrix[28],matrix[29],matrix[0],matrix[1],matrix[2]
        matrix[14], matrix[15] = swapper(matrix[14], matrix[15])
        matrix[18], matrix[20] = swapper(matrix[18], matrix[20])
    elif action is 01:
        matrix[2],matrix[5],matrix[8],matrix[21],matrix[24],matrix[27] = matrix[21],matrix[24],matrix[27],matrix[2],matrix[5],matrix[8]
        matrix[11], matrix[18] = swapper(matrix[11], matrix[18])
        matrix[12], matrix[14] = swapper(matrix[12], matrix[14])
    elif action == 0x2:
        (matrix[6],matrix[7],matrix[8],matrix[21],matrix[22],matrix[23])=(matrix[21],matrix[22],matrix[23],matrix[6],matrix[7],matrix[8])
        matrix[12], matrix[17] = swapper(matrix[12], matrix[17])
        matrix[9], matrix[11] = swapper(matrix[9], matrix[11])
    elif action == 3:
        (matrix[0],matrix[3],matrix[6],matrix[23],matrix[26],matrix[29]) = (matrix[23],matrix[26],matrix[29],matrix[0],matrix[3],matrix[6])
        matrix[9], matrix[20] = swapper(matrix[9], matrix[20])
        matrix[15], matrix[17] = swapper(matrix[15], matrix[17])

def _equlicious(elements, leftx, rightx):
    try:
        return min([elements[i]==elements[leftx] for i in xrange(leftx, rightx)])
    except Exception:
        return False

def iS_Correct(cmpt):
    return (_equlicious(cmpt, 9, 12) and _equlicious(cmpt, 12, 15) and 
        _equlicious(cmpt, 15, 18) and _equlicious(cmpt, 18, 21) and 
        _equlicious(cmpt, 0, 9) and _equlicious(cmpt, 21, 30))

_ANSWER_TO_LIFE = [8]
def _recursolve(state, count, forbidden):
    if _ANSWER_TO_LIFE[0] <= count:
        return
    if iS_Correct(state):
        _ANSWER_TO_LIFE[0] = count
        return
    for idx in [0,1,2,3]:
        if _ANSWER_TO_LIFE[0] <= count+1:
            break
        if idx==forbidden:
            continue
        _fancy_r0tate(state, idx)
        _recursolve(state, count+1, idx)
        _fancy_r0tate(state, idx)

_MAD_INPUT_ = input()
for oh in xrange(_MAD_INPUT_):
    crazy_pile = map(int, raw_input().split())
    _ANSWER_TO_LIFE[0] = 8
    _recursolve(crazy_pile, 0, -1)
    print _ANSWER_TO_LIFE[0]