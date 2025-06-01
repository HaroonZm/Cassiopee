import sys

BIG_NUM = 2000000000
sys.setrecursionlimit(100000)

while True:
    N = int(input())
    if N == 0:
        break
    me = list(map(int, input().split()))
    enemy = list(map(int, input().split()))
    me.sort(reverse=True)
    enemy.sort(reverse=True)
    num_win = 0
    ans = BIG_NUM
    k = 0
    for i in range(N - 1):
        if me[i] > enemy[k]:
            num_win += 1
            if num_win > (i + 1) // 2:
                ans = i + 1
                break
        else:
            k += 1
    if ans == BIG_NUM:
        print("NA")
    else:
        print("%d" % (ans))