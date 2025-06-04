from collections import deque

def solve():
    while True:
        # Lecture du nombre de voies de parking (x) et de lignes d'échange (y)
        x, y = map(int, input().split())
        if x == 0 and y == 0:
            break

        # Structure pour stocker les connexions entre les extrémités
        # Chaque extrémité est identifiée par (ligne, côté) où côté est 'W' ou 'E'
        connections = { (i, 'W'): [], (i, 'E'): [] for i in range(x)}

        for _ in range(y):
            p, q = input().split()
            # p et q sont de la forme "0E", "1W" etc.
            p_line, p_side = int(p[:-1]), p[-1]
            q_line, q_side = int(q[:-1]), q[-1]
            # On ajoute la connexion dans les deux sens
            connections[(p_line, p_side)].append((q_line, q_side))
            connections[(q_line, q_side)].append((p_line, p_side))

        # Lecture des configurations d'arrivée (état initial)
        start = []
        for _ in range(x):
            line = input().strip()
            if line == '-':
                start.append('')
            else:
                start.append(line)

        # Lecture des configurations de départ (état final)
        goal = []
        for _ in range(x):
            line = input().strip()
            if line == '-':
                goal.append('')
            else:
                goal.append(line)

        # BFS pour trouver le nombre minimal de mouvements
        # Etat représenté par un tuple de x chaînes correspondant aux lignes
        start_state = tuple(start)
        goal_state = tuple(goal)

        # Pour éviter de revisiter un état
        visited = set()
        visited.add(start_state)

        queue = deque()
        # Chaque élément = (état, nombre de mouvements)
        queue.append((start_state, 0))

        while queue:
            state, moves = queue.popleft()

            if state == goal_state:
                # Solution optimale trouvée
                print(moves)
                break

            # On explore toutes les possibilités de déplacement d'un (sous-) train
            # sur les lignes d'échange = arêtes entre extrémités

            # Pour chaque ligne de parking i
            for i in range(x):
                train = state[i]
                # Si la ligne est vide, rien à déplacer
                if not train:
                    continue

                # On peut déplacer un sous-train qui est un prefix ou suffix de la ligne
                # associé à une extrémité: côté 'W' correspond au début du string train (Ouest),
                # côté 'E' correspond à la fin du string train (Est).
                #
                # Les sous-trains déplaçables sont :
                # - un segment du début (pour extrémité W)
                # - un segment de fin (pour extrémité E)
                #
                # On peut aussi déplacer la totalité de la ligne (division "à 0" ou "à len(train)")
                # Pour une extrémité donnée, on essaiera toutes les coupures possibles.

                for side in ['W', 'E']:
                    if side == 'W':
                        # On regarde les subdivisions possibles en partant du début
                        for split_pos in range(1, len(train)+1):
                            moved = train[:split_pos]      # sous-train déplacé
                            kept = train[split_pos:]       # reste sur la ligne

                            # Pour chaque ligne connectée à cette extrémité
                            for (dest_line, dest_side) in connections[(i, side)]:
                                dest_train = state[dest_line]

                                # Pour coller, il faut ajouter moved à l'extrémité opposée de dest_side
                                #
                                # L’extrémité où on colle le train déplacé dans la ligne destination est l'extrémité opposée à dest_side,
                                # car le mouvement arrive à cette extrémité.
                                # Exemple : si dest_side == 'W' (extrémité ouest),
                                # alors on ajoute moved à l’extrémité est
                                #
                                # Donc on définit la fonction d'ajout plus bas.

                                new_dest_train = append_train(dest_train, moved, opposite_side(dest_side))

                                # Nouveau état :
                                new_state = list(state)
                                new_state[i] = kept
                                new_state[dest_line] = new_dest_train
                                new_state = tuple(new_state)

                                if new_state not in visited:
                                    visited.add(new_state)
                                    queue.append((new_state, moves + 1))
                    else:  # side == 'E'
                        # subdivisions possibles en partant de la fin
                        for split_pos in range(1, len(train)+1):
                            moved = train[-split_pos:]     # sous-train déplacé
                            kept = train[:-split_pos]      # reste sur la ligne

                            for (dest_line, dest_side) in connections[(i, side)]:
                                dest_train = state[dest_line]
                                new_dest_train = append_train(dest_train, moved, opposite_side(dest_side))

                                new_state = list(state)
                                new_state[i] = kept
                                new_state[dest_line] = new_dest_train
                                new_state = tuple(new_state)

                                if new_state not in visited:
                                    visited.add(new_state)
                                    queue.append((new_state, moves + 1))


# Fonction utilitaire : retourne l'extrémité opposée ('W' <-> 'E')
def opposite_side(side):
    return 'E' if side == 'W' else 'W'

# Fonction utilitaire : ajoute un train 'segment' à une extrémité 'side' de la ligne 'train_line'
# side == 'W' -> ajout au début, == 'E' -> ajout à la fin
def append_train(train_line, segment, side):
    if side == 'W':
        # Ajout au début : segment + train_line
        return segment + train_line
    else:
        # Ajout à la fin : train_line + segment
        return train_line + segment


if __name__ == "__main__":
    solve()