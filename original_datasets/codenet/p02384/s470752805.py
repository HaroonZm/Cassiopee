def North(dice):
    w = dice[0]
    dice[0] = dice[1]
    dice[1] = dice[5]
    dice[5] = dice[4]
    dice[4] = w
    return dice
def East(dice):
    w = Dice[1]
    dice[1] = dice[2]
    dice[2] = dice[4]
    dice[4] = dice[3]
    dice[3] = w
    return dice

def West(dice):
    w = dice[0]
    dice[0] = dice[2]
    dice[2] = dice[5]
    dice[5] = dice[3]
    dice[3] = w
    return dice

maxloop = 4
Ncnt = 0
Ecnt = 0
Wcnt = 0

Dice = input().split()
q = int(input())

CopyDice = Dice

for i1 in range(q):
    Nloop = True
    Eloop = True
    Wloop = True
    Ncnt = 0
    Ecnt = 0
    Wcnt = 0
    I = input().split()
    top = I[0]
    front = I[1]
    while Eloop:
        while Nloop:
            while Wloop:
                if Dice[0] == top and Dice[1] == front:
                    print(Dice[2])
                    Nloop = False
                    Eloop = False
                    Wloop = False
                    break
                Dice = West(Dice)
                Wcnt += 1
                if Wcnt == maxloop:
                    Wloop = False
            Dice = North(Dice)
            Wcnt = 0
            Wloop = True
            Ncnt += 1
            if Ncnt == maxloop:
                Nloop = False
        Dice = East(Dice)
        Ncnt = 0
        Nloop = True
        Ecnt += 1
        if Ecnt == maxloop:
            Eloop = False
    Dice = CopyDice