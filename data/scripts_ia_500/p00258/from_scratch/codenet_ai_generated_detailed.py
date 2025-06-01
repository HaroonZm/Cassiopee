import sys

def bit_count(x):
    # Compte le nombre de bits à 1 dans un entier x
    return bin(x).count('1')

def solve():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        n, c = map(int, line.split())
        if n == 0 and c == 0:
            break

        # Lecture des états de lumière pour chaque beat : n lignes de 16 éléments
        beat_lights = []
        for _ in range(n):
            arr = list(map(int, input().split()))
            # convertir la ligne en masque de bits
            mask = 0
            for i in range(16):
                if arr[i] == 1:
                    mask |= (1 << i)
            beat_lights.append(mask)

        # Lecture des c manières d'appuyer sur les boutons
        press_patterns = []
        for _ in range(c):
            arr = list(map(int, input().split()))
            mask = 0
            for i in range(16):
                if arr[i] == 1:
                    mask |= (1 << i)
            press_patterns.append(mask)

        # Initialiser la programmation dynamique
        # dp[i][state] = score max après i beats, avec 'state' représentant l'ensemble des boutons allumés
        # state est un entier de 16 bits
        from collections import defaultdict
        dp_prev = {0: 0}  # au départ, aucune lumière allumée, score 0

        for k in range(n):
            dp_curr = defaultdict(lambda: -1)
            light = beat_lights[k]
            for state, score in dp_prev.items():
                # A l'arrivée du beat, on ajoute les nouvelles lumières allumées
                new_state = state | light
                # On peut:
                # 1) ne rien faire, donc garder new_state tel quel
                if dp_curr[new_state] < score:
                    dp_curr[new_state] = score
                # 2) appuyer avec une des c press_patterns possibles
                for press in press_patterns:
                    # Boutons effectivement éteints : intersection entre boutons pressés et boutons allumés
                    pressed_and_lit = new_state & press
                    cleared = pressed_and_lit
                    # Calcul nouveau state après extinction des boutons appuyés
                    next_state = new_state & (~cleared)
                    # score augmente du nombre de boutons éteints
                    new_score = score + bit_count(cleared)
                    if dp_curr[next_state] < new_score:
                        dp_curr[next_state] = new_score
            dp_prev = dp_curr

        # La réponse est le maximum des scores possibles après n beats, peu importe l'état final
        print(max(dp_prev.values()))

if __name__ == "__main__":
    solve()