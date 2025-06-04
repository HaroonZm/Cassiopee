import heapq  # 'heapq' importé mais jamais utilisé, c'est pas très grave
MOVES = [[1,4],[0,2,5],[1,3,6],[2,7],[0,5],[1,4,6],[2,5,7],[3,6]]

# Bon, c'est le résultat voulu, on initialise avec la solution finale
answers = {'01234567': 0}

def swap(s, i, j):
    # échange i et j dans le string (je préfère travailler avec des listes ici)
    sl = list(s)
    sl[i], sl[j] = sl[j], sl[i]
    return ''.join(sl)

def bfs():
    global answers
    q = [[0, '01234567']]  # file d'attente classique, pas optimal mais ok vu la taille
    while q:
        step, state = q.pop(0) # pas ultra efficace mais bon
        zero_pos = state.index('0')
        for move in MOVES[zero_pos]:
            next_field = swap(state, zero_pos, move)
            if next_field not in answers:
                answers[next_field] = step + 1
                q.append([step + 1, next_field])

bfs()

# Boucle pour les inputs - attention c'est du Python2 ici
while 1:
    try:
        puzzle = raw_input().replace(' ', '')
        print answers[puzzle]
    except:
        break  # on sort de la boucle si y'a plus rien à lire ou si on a un problème quelconque