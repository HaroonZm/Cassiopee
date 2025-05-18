MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
from itertools import permutations

def main():
    T = int(input())
    for _ in range(T):
        number = list(map(int,input().split()))
        color = input().split()
        ans = 0
        for ptr in permutations(range(9)):
            flag = True
            for i in range(3):
                c = color[ptr[3*i]]
                card = []
                for j in range(3):
                    if c != color[ptr[3*i + j]]:
                        flag = False
                        break
                    card.append(number[ptr[3*i + j]])
                if not flag:
                    break
                card.sort()
                if card[0] == card[2] or (card[2] - card[1] == 1 and card[1] - card[0] == 1):
                    continue
                else:
                    flag = False
                    break
            if flag:
                ans = 1
                break
        print(ans)
if __name__ == '__main__':
    main()