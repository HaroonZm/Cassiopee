def main():
    from heapq import heappop, heappush

    nombre_equipes = int(input())
    scores_par_equipes = [0] * nombre_equipes

    nombre_matchs = nombre_equipes * (nombre_equipes - 1) // 2
    for _ in range(nombre_matchs):
        equipe_a, equipe_b, score_a, score_b = map(int, input().split())
        scores_par_equipes[equipe_a - 1] += 3 * (score_a > score_b) + (score_a == score_b)
        scores_par_equipes[equipe_b - 1] += 3 * (score_b > score_a) + (score_b == score_a)

    file_priorite = []
    for indice, score in enumerate(scores_par_equipes):
        heappush(file_priorite, [-score, indice])

    rang_courant = 1
    rang_affiche = 1
    score_precedent = float('inf')
    classement_final = [0] * nombre_equipes

    while file_priorite:
        score_negatif, indice_equipe = heappop(file_priorite)
        if score_negatif != score_precedent:
            rang_courant = rang_affiche
        classement_final[indice_equipe] = rang_courant
        rang_affiche += 1
        score_precedent = score_negatif

    print(*classement_final, sep='\n')

main()