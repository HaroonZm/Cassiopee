nombre_equipes = int(raw_input())
points_par_equipe = [0] * (nombre_equipes + 1)
nombre_matchs = nombre_equipes * (nombre_equipes - 1) / 2
for _ in range(nombre_matchs):
    equipe_a, equipe_b, score_a, score_b = map(int, raw_input().split())
    if score_a > score_b:
        points_par_equipe[equipe_a] += 3
    elif score_a < score_b:
        points_par_equipe[equipe_b] += 3
    else:
        points_par_equipe[equipe_a] += 1
        points_par_equipe[equipe_b] += 1
for equipe_courante in range(1, nombre_equipes + 1):
    classement = 1
    for equipe_comparaison in range(1, nombre_equipes + 1):
        if points_par_equipe[equipe_courante] < points_par_equipe[equipe_comparaison]:
            classement += 1
    print classement