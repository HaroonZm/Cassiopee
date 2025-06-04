import sys
from sys import stdin
input = stdin.readline

while True:
    m = int(input())
    if m == 0:
        break
    cards = []
    for _ in range(m):
        a, b = map(int, input().split())
        cards.append([a, b])
    g = int(input())
    guesses = []
    for _ in range(g):
        guesses.append(int(input()))
    cards.append([0, 0])
    cards.sort()
    W = max(guesses) + 1
    dp = [0] * W
    dp[0] = 1
    for i in range(1, m+1):
        card_num = cards[i][0]
        card_rem = cards[i][1]
        for j in range(W-1, 0, -1):
            for k in range(1, card_rem+1):
                if card_num * k <= j:
                    dp[j] += dp[j - card_num * k]
    for gg in guesses:
        print(dp[gg])