def score_game(servers, first_server):
    score = {'A': 0, 'B': 0}
    server = first_server
    for s in servers:
        score[s] += 1  # サーブを打った人が得点
        server = s      # 次のサーブは直前のポイントを取った人
        a, b = score['A'], score['B']
        if (a >= 11 or b >= 11) and abs(a - b) >= 2:
            break
    return score['A'], score['B'], server

while True:
    games = [input().strip() for _ in range(3)]
    if games[0] == '0':
        break

    first_servers = ['A']
    results = []
    for i in range(3):
        a, b, winner = score_game(games[i], first_servers[i])
        results.append((a, b))
        if i < 2:
            first_servers.append('A' if a > b else 'B')

    for a, b in results:
        print(a, b)