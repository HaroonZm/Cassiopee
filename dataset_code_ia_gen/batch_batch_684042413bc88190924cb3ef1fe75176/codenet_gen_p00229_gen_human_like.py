while True:
    b, r, g, c, s, t = map(int, input().split())
    if b == 0 and r == 0 and g == 0 and c == 0 and s == 0 and t == 0:
        break

    medals = 100
    # ボーナスゲーム回数は b*5 + r*3
    bonus_games = b*5 + r*3
    normal_games = s
    free_games = c

    # 通常ゲーム：メダル3枚投入
    medals -= normal_games * 3
    # 通常ゲーム中のブドウ揃い：1回につき15枚獲得
    medals += g * 15
    # ボーナスゲーム：1ゲーム2枚投入、必ずブドウ揃いで15枚獲得
    medals -= bonus_games * 2
    medals += bonus_games * 15
    # スター揃いは無料ゲームなのでメダルの増減なし（投入もなし）

    print(medals)