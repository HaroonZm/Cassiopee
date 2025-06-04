dai = list(map(int, input().split()))
daini = list(map(int, input().split()))
def kouten():
    x = dai[0]
    dai[0] = dai[1]
    dai[1] = dai[5]
    dai[5] = dai[4]
    dai[4] = x
def sokuten():
    x = dai[0]
    dai[0] = dai[2]
    dai[2] = dai[5]
    dai[5] = dai[3]
    dai[3] = x
def tokei():
    dai1 = dai[1]
    dai[1] = dai[2]
    dai[2] = dai[4]
    dai[4] = dai[3]
    dai[3] = dai1
def check():
    for j in range(4):
        if daini[0] == dai[0] and daini[1] == dai[1] and daini[2] == dai[2] and daini[3] == dai[3] and daini[4] == dai[4] and daini[5] == dai[5]:
            print('Yes')
            return True
        tokei()
    return False
for a in range(3):
    if not check():
        kouten()
    else:
        break
    if not check():
        sokuten()
    else:
        break
    if a == 2:
        print('No')