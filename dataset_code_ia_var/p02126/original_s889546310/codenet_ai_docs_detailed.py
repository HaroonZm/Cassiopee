import heapq

def main():
    """
    Programme principal pour déterminer la somme maximale des poids d'articles sélectionnés,
    en respectant les contraintes de capacité d'achat par catégorie et la sélection du meilleur
    poids parmi toutes les catégories.
    
    Étapes :
    1. Lecture des entrées : nombre d'articles, nombre d'articles à sélectionner, nombre de catégories.
    2. Initialisation des files à priorité pour chaque catégorie.
    3. Application de la contrainte de capacité par catégorie (nombre de produits achetables par catégorie).
    4. Sélection finale des 'm' meilleurs poids parmi toutes les catégories.
    5. Affichage du résultat.
    """
    # Lecture du nombre total d'articles (n), du nombre d'articles à sélectionner (m),
    # et du nombre de catégories (c)
    n, m, c = map(int, input().split())

    # Création d'une liste de files à priorité (min-heaps) pour chaque catégorie.
    # On ajoute 1 pour que l'indice corresponde à l'identifiant de la catégorie (1-based indexing).
    queues = [[] for _ in range(c + 1)]

    # Lecture des capacités d'achat possibles dans chaque catégorie (can_buy).
    # can_buy[i] représente le nombre maximal d'articles achetables dans la catégorie i.
    # On ajoute un zéro en première position pour que l'indice corresponde à l'identifiant de la catégorie.
    can_buy = [0] + list(map(int, input().split()))

    # Lecture des articles et ajout de leur poids dans la file à priorité de leur catégorie.
    for _ in range(n):
        cat, weight = map(int, input().split())
        # Ajout du poids de l'article dans la file à priorité de la catégorie concernée.
        heapq.heappush(queues[cat], weight)
        # Si la taille dépasse la capacité d'achat, on retire l'élément ayant le plus petit poids.
        if len(queues[cat]) > can_buy[cat]:
            heapq.heappop(queues[cat])

    # Extraction de tous les poids restants de chaque catégorie dans une seule liste.
    # À ce stade, chaque file à priorité contient au maximum 'can_buy' meilleurs poids pour la catégorie.
    selected_weights = [weight for category in queues for weight in category]

    # Tri de tous les poids pour en sélectionner les 'm' meilleurs (poids les plus élevés).
    selected_weights.sort()

    # Calcul de la somme des 'm' meilleurs poids (en partant de la fin de la liste triée).
    answer = sum(selected_weights[-m:])

    # Affichage du résultat final.
    print(answer)

if __name__ == "__main__":
    main()