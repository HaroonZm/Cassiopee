def process_operations():
    """
    Lis les entrées de l'utilisateur et effectue des opérations sur une liste de listes en fonction des instructions reçues.
    Les opérations sont de deux types :
    - Ajouter un nombre à la sous-liste la moins remplie (instruction '1 num')
    - Extraire et enregistrer le premier élément d'une sous-liste donnée (instruction '2 num')
    
    Affiche les résultats des opérations d'extraction à la fin.
    """
    # Lecture de N (nombre de listes) et M (nombre d'opérations)
    N, M = map(int, input().split())
    
    # Initialisation des N listes vides
    L = [[] for _ in range(N)]
    
    # Liste pour stocker les résultats des opérations d'extraction
    ans = []
    
    # Traitement des M opérations
    for i in range(M):
        # Lecture de chaque instruction et possible valeur associée
        info, num = map(int, input().split())
        
        if info == 1:
            # Instruction 1: ajouter 'num' à la sous-liste ayant le moins d'éléments
            x = 0  # On part de la première liste
            for j in range(1, N):
                # On cherche la liste avec la plus petite taille
                if len(L[j]) < len(L[x]):
                    x = j
            # Ajout de 'num' à la sous-liste choisie
            L[x].append(num)
        else:
            # Instruction 2: extraire le premier élément de la sous-liste (num-1)
            ans.append(L[num-1][0])  # Ajout du premier élément à la liste de réponses
            del L[num-1][0]          # Suppression de l'élément extrait
            
    # Affichage de toutes les réponses stockées lors des suppressions
    print(*ans, sep='\n')

# Lancement du traitement
process_operations()