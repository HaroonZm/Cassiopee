import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop
import copy
from test.support import _MemoryWatchdog

BIG_NUM = 2000000000
HUGE_NUM = 99999999999999999
MOD = 1000000007
EPS = 0.000000001
sys.setrecursionlimit(100000)

class Type(Enum):
    TRUE = 0
    FALSE = 1
    UNDEFINED = 2

MIN = 1
MAX = 13

dp = [[[None] * 2 for _ in range(15)] for _ in range(15)]

def recursive(L, R, Sente, Gote, rest_Sente, rest_Gote, is_Sente):
    if dp[L][R][is_Sente] != Type.UNDEFINED:
        return dp[L][R][is_Sente] == Type.TRUE

    if rest_Sente == 0:
        return True
    elif rest_Gote == 0:
        return False

    if is_Sente == True:
        if (L < MIN or (L >= MIN and Sente[L] == False)) and (R > MAX or (R <= MAX and Sente[R] == False)):
            return recursive(L, R, Sente, Gote, rest_Sente, rest_Gote, False)
        else:
            ret = False
            next_Sente = [None] * 14
            for i in range(MIN, MAX + 1):
                next_Sente[i] = Sente[i]
            if L >= MIN and Sente[L] == True:
                next_Sente[L] = False
                ret |= recursive(L - 1, R, next_Sente, Gote, rest_Sente - 1, rest_Gote, False)
                next_Sente[L] = True
            if R <= MAX and Sente[R] == True:
                next_Sente[R] = False
                ret |= recursive(L, R + 1, next_Sente, Gote, rest_Sente - 1, rest_Gote, False)
            if ret == True:
                dp[L][R][is_Sente] = Type.TRUE
            else:
                dp[L][R][is_Sente] = Type.FALSE
            return ret
    else:
        if (L < MIN or (L >= MIN and Gote[L] == False)) and (R > MAX or (R <= MAX and Gote[R] == False)):
            return recursive(L, R, Sente, Gote, rest_Sente, rest_Gote, True)
        else:
            ret = True
            next_Gote = [None] * 14
            for i in range(MIN, MAX + 1):
                next_Gote[i] = Gote[i]
            if L >= MIN and Gote[L] == True:
                next_Gote[L] = False
                ret &= recursive(L - 1, R, Sente, next_Gote, rest_Sente, rest_Gote - 1, True)
                next_Gote[L] = True
            if R <= MAX and Gote[R] == True:
                next_Gote[R] = False
                ret &= recursive(L, R + 1, Sente, next_Gote, rest_Sente, rest_Gote - 1, True)
            if ret == True:
                dp[L][R][is_Sente] = Type.TRUE
            else:
                dp[L][R][is_Sente] = Type.FALSE
            return ret

N = int(input())

for _ in range(N):
    Sente = [False] * 14
    Gote = [None] * 14
    for L in range(0, 7):
        for R in range(8, 15):
            dp[L][R][True] = Type.UNDEFINED
            dp[L][R][False] = Type.UNDEFINED
    tmp_input = list(map(int, input().split()))
    for i in range(len(tmp_input)):
        Sente[tmp_input[i]] = True
    for i in range(MIN, MAX + 1):
        Gote[i] = not Sente[i]
    if recursive(6, 8, Sente, Gote, 6, 6, True) == True:
        print("yes")
    else:
        print("no")