import sys

sys.setrecursionlimit(10**7)

N = int(input())
S = input()
P = list(map(int, input().split()))
M = 2**N

# Fonction pour simuler le tournoi et retourner le gagnant
def play(players):
    while len(players) > 1:
        next_round = []
        for i in range(0, len(players), 2):
            x = players[i]
            y = players[i+1]
            diff = y - x
            # S est indexé à partir de 0, on accède donc à S[diff-1]
            if S[diff-1] == '0':
                winner = x
            else:
                winner = y
            next_round.append(winner)
        players = next_round
    return players[0]

for k in range(M):
    rotated = P[k:] + P[:k]
    print(play(rotated))