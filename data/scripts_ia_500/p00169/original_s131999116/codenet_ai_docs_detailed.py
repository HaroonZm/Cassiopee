def solve():
    """
    Lit une liste de valeurs entières depuis l'entrée standard représentant des cartes,
    limite chaque carte à une valeur maximale de 10 (règle du Blackjack),
    puis calcule la somme maximale possible des cartes sans dépasser 21 en tenant compte
    qu'un As (valeur 1) peut valoir soit 1 soit 11.
    
    Retourne 1 si l'entrée contient uniquement 0 (condition d'arrêt), sinon imprime le résultat.
    
    Comportement détaillé :
    - Si la liste contient uniquement 0, la fonction retourne 1 pour signaler l'arrêt.
    - Si la liste contient plus de 21 cartes, imprime 0 et retourne 0, considérant la main invalide.
    - Sinon, parcourt toutes les combinaisons possibles en remplaçant chaque As par 1 ou 11,
      calcule la somme totale de la main et retient la plus élevée sans dépasser 21.
    - Imprime cette valeur maximale obtenue.
    """
    # Lecture des valeurs des cartes depuis l'entrée, séparées par espaces
    c = list(map(int, input().split()))
    
    # Limite la valeur maximale à 10 pour chaque carte (les figures valent 10)
    c = [min(10, e) for e in c]
    
    # Condition d'arrêt : si la liste contient seulement un 0, retourne 1 pour sortir du programme
    if c == [0]:
        return 1
    
    # Si plus de 21 cartes, la main est invalide => affiche 0 et continue le programme (retourne 0)
    if len(c) > 21:
        print(0)
        return 0
    else:
        ans = 0  # Variable pour stocker la meilleure somme possible sans dépasser 21
        # Parcours toutes les combinaisons possibles pour déterminer la valeur des As
        # Chaque bit de 'bit' représente si l'As à l'indice i vaut 1 (bit=0) ou 11 (bit=1)
        for bit in range(1 << len(c)):
            s = 0  # Somme courante des valeurs des cartes pour cette combinaison
            for i in range(len(c)):
                if c[i] != 1:
                    # Cartes autres que l'As ont une valeur fixe
                    s += c[i]
                else:
                    # Pour un As (valeur 1), on choisit entre 1 ou 11 selon le bit correspondant
                    if bit >> i & 1:
                        s += 11
                    else:
                        s += 1
            # Ne retient que les sommes inférieures ou égales à 21
            if s <= 21:
                ans = max(ans, s)
        # Affiche la meilleure somme obtenue sans dépasser 21
        print(ans)
        return 0

def main():
    """
    Fonction principale qui exécute la fonction solve en boucle
    jusqu'à ce que celle-ci retourne 1, condition de terminaison.
    """
    while solve() == 0:
        pass

if __name__ == '__main__':
    main()