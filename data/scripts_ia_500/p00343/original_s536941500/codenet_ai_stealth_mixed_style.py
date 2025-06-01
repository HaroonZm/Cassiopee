import heapq
from enum import Enum
import sys

sys.setrecursionlimit(100000)

BIG_NUM = 2000000000
HUGE_NUM = 99999999999999999
MOD = 1000000007
EPS = 1e-9

class Type(Enum):
    TRUE = 0
    FALSE = 1
    UNDEFINED = 2

MIN = 1
MAX = 13

dp = [[[Type.UNDEFINED for _ in range(2)] for __ in range(15)] for ___ in range(15)]

def recursive(L,R,Sente,Gote,rest_Sente,rest_Gote,is_Sente):
    if dp[L][R][is_Sente] != Type.UNDEFINED:
        return dp[L][R][is_Sente] == Type.TRUE

    if rest_Sente == 0:
        return True
    elif rest_Gote == 0:
        return False

    if is_Sente:
        if (L < MIN or (L >= MIN and not Sente[L])) and (R > MAX or (R <= MAX and not Sente[R])):
            return recursive(L,R,Sente,Gote,rest_Sente,rest_Gote,False)
        else:
            ret = False
            next_Sente = Sente[:]
            if L >= MIN and Sente[L]:
                next_Sente[L] = False
                ret |= recursive(L-1,R,next_Sente,Gote,rest_Sente-1,rest_Gote,False)
                next_Sente[L] = True
            if R <= MAX and Sente[R]:
                next_Sente[R] = False
                ret |= recursive(L,R+1,next_Sente,Gote,rest_Sente-1,rest_Gote,False)
            dp[L][R][is_Sente] = Type.TRUE if ret else Type.FALSE
            return ret
    else:
        if (L < MIN or (L >= MIN and not Gote[L])) and (R > MAX or (R <= MAX and not Gote[R])):
            return recursive(L,R,Sente,Gote,rest_Sente,rest_Gote,True)
        else:
            ret = True
            next_Gote = [None]*14
            for i in range(14):
                next_Gote[i] = Gote[i]
            if L >= MIN and Gote[L]:
                next_Gote[L] = False
                ret &= recursive(L-1,R,Sente,next_Gote,rest_Sente,rest_Gote-1,True)
                next_Gote[L] = True
            if R <= MAX and Gote[R]:
                next_Gote[R] = False
                ret &= recursive(L,R+1,Sente,next_Gote,rest_Sente,rest_Gote-1,True)
            dp[L][R][is_Sente] = Type.TRUE if ret else Type.FALSE
            return ret

def main():
    N = int(sys.stdin.readline())
    for _ in range(N):
        Sente = [False for _ in range(14)]
        Gote = [None]*14

        for L in range(0,7):
            for R in range(8,15):
                dp[L][R][True] = Type.UNDEFINED
                dp[L][R][False] = Type.UNDEFINED

        tmp_input = list(map(int,sys.stdin.readline().split()))
        for val in tmp_input:
            Sente[val] = True
        for i in range(MIN,MAX+1):
            Gote[i] = not Sente[i]

        result = recursive(6,8,Sente,Gote,6,6,True)
        print("yes" if result else "no")

if __name__ == "__main__":
    main()