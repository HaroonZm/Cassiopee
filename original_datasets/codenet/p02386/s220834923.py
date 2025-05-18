# Aizu Problem ITP_1_11_D: Dice IV
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input2.txt", "rt")

a = [0,2,5,3]
b = [0,1,5,4]
c = [1,2,4,3]

def sortdice(dice1,dice2,p,q,r):
    for i in range(4):
        dice1[p[0]],dice1[p[1]],dice1[p[2]],dice1[p[3]]=dice1[p[1]],dice1[p[2]],dice1[p[3]],dice1[p[0]]
        for j in range(4):
            dice1[q[0]],dice1[q[1]],dice1[q[2]],dice1[q[3]]=dice1[q[1]],dice1[q[2]],dice1[q[3]],dice1[q[0]]
            for k in range(4):
                dice1[r[0]],dice1[r[1]],dice1[r[2]],dice1[r[3]]=dice1[r[1]],dice1[r[2]],dice1[r[3]],dice1[r[0]]
                if dice1==dice2:
                    return True
    return False

def all_different(N, dices):
    for i in range(N - 1):
        dice1 = dices[i]
        for j in range(i + 1, N):
            dice2 = dices[j]
            if sortdice(dice1, dice2, a, b, c):
                return False
    return True

    
N = int(input())
dices = []
for _ in range(N):
    dices.append(list(map(int,input().split())))
print("Yes" if all_different(N, dices) else "No")