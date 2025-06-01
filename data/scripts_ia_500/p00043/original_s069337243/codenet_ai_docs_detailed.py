def is_solved(nums):
    """
    Vérifie si une liste de nombres peut être complètement divisée en groupes spécifiques selon les règles suivantes :
    - Groupes de paires de nombres identiques (au moins deux fois le même nombre).
    - Groupes de quatre nombres identiques, accompagnés d'une séquence consécutive de deux nombres (key+1 et key+2).
    - Groupes de trois nombres identiques.
    - Groupes de séquences consécutives de trois nombres identiques (ex: key, key+1, key+2).
    
    Args:
        nums (list of int): Liste des nombres à analyser.
    
    Returns:
        bool: True si la liste peut être divisée en groupes conformes aux règles, False sinon.
    """
    keys = set(nums)  # Récupère les valeurs uniques dans la liste pour éviter les calculs redondants
    
    # Parcourt chaque valeur unique pour vérifier les conditions basées sur les paires
    for key in keys:
        if nums.count(key) >= 2:
            tmp = nums[:]  # Crée une copie de la liste pour manipulation sans affecter l'original
            tmp.remove(key)  # Retire deux éléments identiques
            tmp.remove(key)
            
            # Essaye de regrouper le reste de la liste en suivant les différentes règles définies
            for key in keys:
                key_count = tmp.count(key)  # Compte les occurrences de l'élément courant
                
                if key_count == 4:
                    # Si on a quatre occurrences identiques, vérifie la présence des éléments consécutifs
                    if key + 1 in tmp and key + 2 in tmp:
                        for _ in range(4):
                            tmp.remove(key)  # Retire les quatre éléments identiques
                        tmp.remove(key + 1)  # Retire les deux éléments consécutifs
                        tmp.remove(key + 2)
                        
                elif key_count == 3:
                    # Retire un groupe de trois éléments identiques
                    for _ in range(3):
                        tmp.remove(key)
                        
                elif tmp.count(key + 1) >= key_count and tmp.count(key + 2) >= key_count:
                    # Retire des groupes consécutifs formés par key, key+1 et key+2
                    for _ in range(key_count):
                        tmp.remove(key)
                        tmp.remove(key + 1)
                        tmp.remove(key + 2)
            
            # Si tout a été retiré, la liste est bien divisée selon les règles
            if tmp == []:
                return True
    
    # Si aucune condition n'a permis de vider la liste, on retourne False
    return False


while True:
    try:
        # Lit une entrée utilisateur, la convertit en liste d'entiers (chiffres séparés)
        puzzle = list(map(int, list(input())))
        ans = []  # Liste pour stocker les solutions possibles
        
        # Teste pour chaque chiffre possible (1 à 9) s'il peut être ajouté pour rendre la liste solvable
        for i in range(1, 10):
            if puzzle.count(i) <= 3 and is_solved(puzzle + [i]):
                ans.append(i)  # Ajoute le chiffre si la condition est vraie
        
        # Affiche la liste des chiffres possibles ou 0 si aucune solution
        if ans:
            print(*ans)
        else:
            print(0)
    
    # Gestion de la fin d'entrée pour arrêter la boucle proprement
    except EOFError:
        break