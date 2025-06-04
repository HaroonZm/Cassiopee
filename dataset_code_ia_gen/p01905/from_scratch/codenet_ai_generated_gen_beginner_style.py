N, M = map(int, input().split())
withdraw = set()
for _ in range(M):
    a = int(input())
    withdraw.add(a)

players = []
for i in range(N):
    if i not in withdraw:
        players.append(i)

matches = 0

while len(players) > 1:
    next_round = []
    i = 0
    while i < len(players):
        if i+1 < len(players):
            # Deux joueurs s'affrontent, un match a lieu
            matches += 1
            # On choisit arbitrairement le joueur i comme vainqueur
            next_round.append(players[i])
            i += 2
        else:
            # Un joueur passe ce tour sans jouer
            next_round.append(players[i])
            i += 1
    players = next_round

print(matches)