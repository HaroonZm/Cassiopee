def solve(n, l, r, A):
    """
    Calcule le nombre d'entiers x dans l'intervalle [l, r] qui satisfont une condition de divisibilité 
    particulière basée sur le tableau A de taille n.
    
    Pour chaque x de [l, r] :
        - On cherche le premier A[i] qui divise x.
        - Si trouvé, on ajoute 1 au résultat si i (l'indice) est pair, sinon 0, puis on arrête de chercher.
        - Si aucun A[i] ne divise x, on ajoute 1 au résultat si n (la taille de A) est pair, sinon 0.
    
    Args:
        n (int): La taille du tableau A.
        l (int): Borne inférieure de l'intervalle (inclus).
        r (int): Borne supérieure de l'intervalle (inclus).
        A (list of int): Tableau des diviseurs à tester pour chaque x.
        
    Returns:
        int: Le total cumulé selon la logique décrite ci-dessus.
    """
    res = 0  # Initialise le compteur de résultats
    for x in range(l, r + 1):  # Parcourt tous les x de l à r inclus
        for i in range(n):     # Parcourt chaque élément de A
            if x % A[i] == 0:  # Si x est divisible par A[i]
                # Ajoute 1 si l'indice i est pair, sinon 0
                res += 1 if (i % 2 == 0) else 0
                break  # Passe à l'entier x suivant
        else:
            # Si aucun diviseur n'est trouvé, ajoute 1 si n est pair, sinon 0
            res += 1 if (n % 2 == 0) else 0
    return res

def main():
    """
    Point d'entrée du programme.
    
    Lit des séries de jeux de test depuis l'entrée standard, chaque jeu de test étant constitué de trois 
    entiers n, l, r suivi de n entiers pour compléter le tableau A.
    
    S'arrête à la lecture d'une ligne contenant trois zéros.
    Pour chaque jeu de test, utilise la fonction solve pour calculer et stocker la réponse. 
    Ensuite, affiche les résultats de tous les jeux de test dans l'ordre de lecture.
    """
    ans = []  # Liste stockant les résultats pour chaque jeu de test
    while True:
        # Lit et décompose n, l, r pour un jeu de test
        n, l, r = map(int, input().split())
        # Arrêt si la ligne est la sentinelle demandée (0, 0, 0)
        if n == 0 and l == 0 and r == 0:
            break
        # Construction du tableau A à partir de l'entrée utilisateur
        A = [int(input()) for _ in range(n)]
        # Calcul du résultat et ajout à la liste des réponses
        ans.append(solve(n, l, r, A))
    # Affiche chacun des résultats trouvés
    for result in ans:
        print(result)

main()