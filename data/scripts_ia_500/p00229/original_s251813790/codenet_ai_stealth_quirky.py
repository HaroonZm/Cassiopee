import sys
fi = sys.stdin

def calculate_coins():
    starting_coins = 100
    while True:
        data = fi.readline().strip()
        if not data:
            break
        seven_val, bar_val, grape_val, cherry_val, star_val, total_games = map(int, data.split())
        if all(x == 0 for x in (seven_val, bar_val, grape_val, cherry_val, star_val, total_games)):
            return
        free_play = star_val
        bonus_play = seven_val * 5 + bar_val * 3
        normal_play = total_games - free_play - bonus_play

        coins_after_bonuses = starting_coins - (bonus_play * 2) - (normal_play * 3)
        coins_after_rewards = coins_after_bonuses + (bonus_play + seven_val + bar_val) * 15 + grape_val * 7 + cherry_val * 2

        print(coins_after_rewards)

calculate_coins()