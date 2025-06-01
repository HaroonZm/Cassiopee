"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0154

"""
import sys
from sys import stdin
input = stdin.readline

def solve(m, cards, g, guesses):
    ans = []

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
                if card_num*k <= j:
                    dp[j] += dp[j-card_num*k]

    for gg in guesses:
        ans.append(dp[gg])
    return ans

def main(args):
    # m = 5
    # cards = [[1, 10], [5, 3], [10, 3], [25, 2], [50, 2]]
    # g = 4
    # guesses = [120, 500, 100, 168]

    while True:
        m = int(input())
        if m == 0:
            break
        cards = []
        for _ in range(m):
            a, b = map(int, input().split())
            cards.append([a, b])
        g = int(input())
        guesses = [int(input()) for _ in range(g)]
        ans = solve(m, cards, g, guesses)
        print(*ans, sep='\n')

if __name__ == '__main__':
    main(sys.argv[1:])