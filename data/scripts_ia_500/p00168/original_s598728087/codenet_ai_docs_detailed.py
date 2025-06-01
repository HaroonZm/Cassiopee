def compute_steps(n):
    """
    Calcule le nombre minimal d'intervalles de 3650 unités nécessaires pour couvrir la valeur B[n].
    
    La séquence B est définie par :
        B[0] = 1
        B[1] = 1
        B[2] = 2
        Pour i >= 3, B[i] = B[i-1] + B[i-2] + B[i-3]
        
    Cette fonction retourne le nombre minimal d'intervalles de taille 3650
    nécessaires pour atteindre ou dépasser B[n].
    
    Args:
        n (int): L'indice pour lequel calculer la valeur.
    
    Returns:
        int: Le nombre minimal d'intervalles de taille 3650 couvrant B[n].
    """
    if n == 0:
        # Pour n=0, B[0]=1, donc on a besoin d'un intervalle minimum.
        return 1
    elif n == 1:
        # Pour n=1, la valeur est aussi 1, donc 1 intervalle.
        return 1
    else:
        # Initialisation de la liste B pour stocker les valeurs jusqu'à l'indice n.
        B = [0] * (n + 1)
        B[0], B[1], B[2] = 1, 1, 2
        
        # Calcul des valeurs de la séquence selon la relation de récurrence.
        for i in range(3, n + 1):
            B[i] = B[i - 1] + B[i - 2] + B[i - 3]
        
        # Calcul du nombre d'intervalles de taille 3650 nécessaires pour B[n].
        if B[n] % 3650 == 0:
            # Si B[n] est un multiple exact de 3650, division entière directe.
            return B[n] // 3650
        else:
            # Sinon, on arrondit à l'entier supérieur (nombre minimal couvrant).
            return B[n] // 3650 + 1

def main():
    """
    Fonction principale qui lit des entiers depuis l'entrée standard jusqu'à la lecture d'un 0,
    calcule pour chaque entier le nombre minimal d'intervalles de 3650 couvrant la valeur de la séquence, 
    et affiche le résultat.
    """
    while True:
        n = int(input())
        if n == 0:
            # Fin du programme si l'entrée est 0.
            break
        else:
            # Calcul et affichage du résultat pour la valeur entrée.
            result = compute_steps(n)
            print(result)

if __name__ == "__main__":
    main()