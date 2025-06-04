def count_red_balls(n, m, xy):
    """
    Calcule le nombre de boules rouges restantes après une série de transferts de boules entre des boîtes.
    
    Args:
        n (int): Nombre total de boîtes, numérotées de 1 à n.
        m (int): Nombre d'opérations de transfert.
        xy (List[List[int]]): Une liste de paires [x, y] représentant le transfert d'une boule de la boîte x à la boîte y.
        
    Returns:
        int: Le nombre de boîtes qui peuvent contenir une boule rouge à la fin des opérations.
    """
    # Initialisation : chaque boîte contient une boule sauf l'indice 0 (non utilisé)
    ball = [1] * (n + 1)  # ball[i] : nombre de boules dans la boîte i
    # Indicateur pour une boule rouge dans chaque boîte : 1 pour vrai, 0 pour faux
    red = [0] * (n + 1)
    # La première boîte commence avec la boule rouge
    red[1] = 1

    # Traitement de chaque opération de transfert
    for x, y in xy:
        # Retirer une boule de la boîte x
        ball[x] -= 1
        # Ajouter une boule à la boîte y
        ball[y] += 1

        # Si la boîte x possède une boule rouge
        if red[x] == 1:
            # La boîte y possède désormais potentiellement une boule rouge
            red[y] = 1
            # Si la boîte x n'a plus de boules après ce transfert
            if ball[x] == 0:
                # Elle ne peut plus contenir la boule rouge
                red[x] = 0

    # Calcul du nombre de boîtes pouvant contenir une boule rouge
    return sum(red)

def main():
    """
    Lit les entrées utilisateur, effectue les transferts de boules et affiche le résultat.
    """
    # Lecture des valeurs n (nombre de boîtes) et m (nombre d'opérations)
    n, m = map(int, input().split())
    # Lecture des m lignes représentant les opérations de transfert
    xy = [list(map(int, input().split())) for _ in range(m)]
    # Appel de la fonction principale et affichage du résultat
    print(count_red_balls(n, m, xy))

if __name__ == "__main__":
    main()