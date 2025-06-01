import sys
reader = sys.stdin.readline

def calculate():
    while True:
        data = reader().split()
        values = list(map(int, data))
        if all(v == 0 for v in values):
            break
        seven, bar, grape, cherry, star, all_game = values
        init_coin = 100
        free_game = star
        bonus_game = 5 * seven + 3 * bar
        nomal_game = all_game - free_game - bonus_game

        last_coin = init_coin
        last_coin -= bonus_game * 2
        last_coin -= nomal_game * 3
        last_coin += (bonus_game + seven + bar) * 15
        last_coin += grape * 7
        last_coin += cherry * 2

        print(last_coin)

calculate()