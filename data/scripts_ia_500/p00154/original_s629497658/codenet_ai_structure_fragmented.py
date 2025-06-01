import sys
from sys import stdin
input = stdin.readline

def read_m():
    return int(input())

def read_cards(m):
    cards = []
    for _ in range(m):
        a, b = read_card_line()
        cards.append([a, b])
    return cards

def read_card_line():
    return map(int, input().split())

def read_g():
    return int(input())

def read_guesses(g):
    guesses = []
    for _ in range(g):
        guesses.append(read_guess())
    return guesses

def read_guess():
    return int(input())

def append_dummy_card(cards):
    cards.append([0, 0])

def sort_cards(cards):
    cards.sort()

def find_max_guess_plus_one(guesses):
    return max(guesses) + 1

def initialize_dp(W):
    dp = [0] * W
    dp[0] = 1
    return dp

def update_dp(dp, cards, m, W):
    for i in range(1, m+1):
        card_num = get_card_num(cards, i)
        card_rem = get_card_rem(cards, i)
        update_dp_for_card(dp, card_num, card_rem, W)
    return dp

def get_card_num(cards, i):
    return cards[i][0]

def get_card_rem(cards, i):
    return cards[i][1]

def update_dp_for_card(dp, card_num, card_rem, W):
    for j in range(W-1, 0, -1):
        update_dp_for_count(dp, card_num, card_rem, j)

def update_dp_for_count(dp, card_num, card_rem, j):
    for k in range(1, card_rem+1):
        if card_num * k <= j:
            dp[j] += dp[j - card_num * k]

def collect_answers(dp, guesses):
    ans = []
    for gg in guesses:
        ans.append(dp[gg])
    return ans

def solve(m, cards, g, guesses):
    append_dummy_card(cards)
    sort_cards(cards)
    W = find_max_guess_plus_one(guesses)
    dp = initialize_dp(W)
    dp = update_dp(dp, cards, m, W)
    ans = collect_answers(dp, guesses)
    return ans

def main_loop():
    while True:
        m = read_m()
        if is_zero(m):
            break
        cards = read_cards(m)
        g = read_g()
        guesses = read_guesses(g)
        ans = solve(m, cards, g, guesses)
        output_answers(ans)

def is_zero(value):
    return value == 0

def output_answers(ans):
    print(*ans, sep='\n')

def main(args):
    main_loop()

if __name__ == '__main__':
    main(sys.argv[1:])