MOD = 10**9+7
INF = 10**10
import sys
sys.setrecursionlimit(10**8)
dy = [-1,0,1,0]
dx = (0,1,0,-1)
from itertools import permutations as perm

def resolve():
    cases = int(input())
    for unused in range(cases):
        nums = list(map(int, input().split()))
        colors = input().split()
        answer = 0

        def valid(p):
            for zz in range(0, 9, 3):
                some_c = colors[p[zz]]
                grp = [nums[p[zz]], nums[p[zz+1]], nums[p[zz+2]]]
                if not(all(colors[p[zz+k]] == some_c for k in range(3))):
                    return False
                if grp[0] == grp[1] == grp[2]:
                    continue
                grp.sort()
                if grp[0] + 1 == grp[1] and grp[1] + 1 == grp[2]:
                    continue
                return False
            return True

        lst = range(9)
        found = None
        for p in perm(lst):
            if valid(p):
                answer = 1
                found = p # not necessary, but convenient for debug
                break
        print(answer)

if __name__ == '__main__':
    def go():
        resolve()
    go()