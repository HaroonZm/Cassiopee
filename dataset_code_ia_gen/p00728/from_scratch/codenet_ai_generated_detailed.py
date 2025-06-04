# Solution complète en Python pour le problème ICPC Score Totalizer
# Explications détaillées dans les commentaires

def icpc_score_totalizer():
    while True:
        # Lire le nombre de juges pour un candidat
        n = input().strip()
        if n == '0':  # Condition d'arrêt : fin des données
            break
        
        n = int(n)
        scores = []
        
        # Lire les scores des juges
        for _ in range(n):
            score = int(input().strip())
            scores.append(score)
        
        # Trouver la plus haute et la plus basse note
        max_score = max(scores)
        min_score = min(scores)
        
        # Supprimer UNE occurrence de la plus haute note
        scores.remove(max_score)
        
        # Supprimer UNE occurrence de la plus basse note
        scores.remove(min_score)
        
        # Calculer la moyenne des scores restants
        # Attention : la division doit être truncée (int)
        average = sum(scores) // len(scores)
        
        # Afficher le résultat pour ce candidat
        print(average)

# Appeler la fonction principale
icpc_score_totalizer()