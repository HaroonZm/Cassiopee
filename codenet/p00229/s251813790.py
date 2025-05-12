import sys
f = sys.stdin

while True:
    seven, bar, grape, cherry, star, all_game = map(int, f.readline().split())
    if seven == bar == grape == cherry == star == all_game == 0:
        break
        
    init_coin = 100
    free_game = star        
    bonus_game = seven * 5 + bar * 3
    nomal_game = all_game - free_game - bonus_game

    last_coin = init_coin - bonus_game * 2 - nomal_game * 3 + (bonus_game + seven + bar) * 15 + grape * 7 + cherry * 2
    print(last_coin)