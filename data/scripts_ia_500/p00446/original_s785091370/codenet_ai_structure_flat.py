import sys
from bisect import bisect_right

while True:
    n = int(input())
    if n == 0:
        break
    taro = sorted([int(input()) for _ in range(n)])
    hanako = sorted(set(range(1, 2*n+1)) - set(taro))
    ba = taro.pop(0)
    player = hanako
    while taro and hanako:
        i = bisect_right(player, ba)
        if i != len(player):
            ba = player.pop(i)
        else:
            player = taro if player == hanako else hanako
            ba = player.pop(0)
        player = taro if player == hanako else hanako
    print(len(hanako))
    print(len(taro))