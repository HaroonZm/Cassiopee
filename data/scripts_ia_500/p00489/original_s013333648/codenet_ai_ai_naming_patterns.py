def calculer_classements():
    from heapq import heappop, heappush
    
    nombre_equipes = int(input())
    scores_par_equipe = [0] * nombre_equipes
    
    nombre_matchs = nombre_equipes * (nombre_equipes - 1) // 2
    for _ in range(nombre_matchs):
        equipe_a, equipe_b, score_a, score_b = map(int, input().split())
        scores_par_equipe[equipe_a - 1] += 3 * (score_a > score_b) + (score_a == score_b)
        scores_par_equipe[equipe_b - 1] += 3 * (score_b > score_a) + (score_a == score_b)
        
    classement_par_score = [[] for _ in range(3 * nombre_equipes)]
    
    for index_equipe, score in enumerate(scores_par_equipe):
        classement_par_score[score].append(index_equipe)
        
    tas_priorite = []
    for index_equipe, score in enumerate(scores_par_equipe):
        heappush(tas_priorite, [-score, index_equipe])
        
    rang_actuel = 1
    rang_affichage = 1
    score_precedent = float('inf')
    
    classement_final = [0] * nombre_equipes
    while tas_priorite:
        score_negatif, index_equipe = heappop(tas_priorite)
        if score_negatif != score_precedent:
            rang_actuel = rang_affichage
        classement_final[index_equipe] = rang_actuel
        rang_affichage += 1
        score_precedent = score_negatif
        
    print(*classement_final, sep='\n')

calculer_classements()