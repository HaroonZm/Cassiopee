# Définition de la fonction principale du programme
def main():
    # Lecture d'une ligne de l'entrée standard, découpage en deux valeurs séparées par un espace,
    # conversion de ces deux valeurs en entiers et assignation à n et m.
    n, m = map(int, input().split())
    
    # Initialisation d'une liste 'st' contenant m sous-listes,
    # chaque sous-liste correspondant à une entrée (arête) lue sur une ligne,
    # transformée en deux entiers (a et b).
    # L'utilisation de [0]*m permet de répéter la saisie m fois à l'aide d'une liste factice de taille m.
    st = [list(map(int, input().split())) for _ in [0]*m]
    
    # Création d'une liste de n listes vides pour représenter les arcs sortants de chaque sommet (graphe orienté)
    g = [[] for _ in [0]*n]
    
    # Pour chaque couple (a, b) dans st, on ajoute b-1 à la liste des voisins du sommet a-1
    # (indices ramenés à zéro pour l'indexation Python)
    [g[a-1].append(b-1) for a, b in st]
    
    # Initialisation de trois listes de taille n remplies de zéros.
    # toP pour stocker le nombre de façons d'atteindre le sommet i depuis la source
    # toE pour conserver la somme des longueurs de chemins accumulées vers i
    # fromE pour le calcul rétrograde des espérances depuis chaque sommet
    toP = [0]*n
    toE = [0]*n
    fromE = [0]*n
    
    # On met à 1 le nombre de façons d'atteindre le point de départ (sommet 0)
    toP[0] = 1
    
    # Boucle pour propager de gauche à droite (du sommet 0 au n-2) les valeurs de toP et toE
    for i in range(n-1):
        # p est le nombre de façons d'arriver à i
        p = toP[i]
        # Si p > 0, c'est-à-dire s'il y a au moins un chemin vers i
        if p > 0:
            # On divise toE[i] (la somme accumulée des longueurs pour arriver à i) par p
            toE[i] /= toP[i]
        # e est maintenant l'espérance depuis la racine jusqu'à i
        e = toE[i]
        # l est le nombre de voisins directs de i (nombre de sorties de i)
        l = len(g[i])
        # Pour chaque voisin j du sommet i
        for j in g[i]:
            # On ajoute à toP[j] la fraction p/l (répartition équitable entre voisins)
            toP[j] += p/l
            # On ajoute à toE[j] la valeur de l'espérance totale du prédecesseur + 1 (coût d'un pas), pondérée par p/l
            toE[j] += (e+1)*p/l
    
    # Deuxième passage, cette fois à rebours, pour calculer l'espérance du sous-graphe à partir de chaque sommet
    for i in range(n-2, -1, -1):
        # l est le nombre d'arcs sortants de i
        l = len(g[i])
        # Pour chaque voisin j du sommet i
        for j in g[i]:
            # On ajoute à fromE[i] la contribution moyenne résultant du voisin (fromE[j]) + 1 (coût du pas),
            # le tout divisé par l pour l'espérance
            fromE[i] += (fromE[j]+1)/l
    
    # On récupère l'espérance totale depuis la racine, stockée dans fromE[0]
    allE = fromE[0]
    # On initialise la réponse avec cette espérance de base
    ans = fromE[0]
    
    # On construit une liste tf, où chaque élément correspond à une "contribution totale d'une arête"
    # pour chaque sommet i, impliquant le nombre de façons d'atteindre i, le coût pour y arriver,
    # et la somme de toutes les espérances pour ses voisins
    tf = [
        toP[i]*(
            (toE[i]+1)*len(g[i])+            # Somme des coûts des chemins sortants du sommet i
            sum([fromE[j] for j in g[i]])    # Somme des espérances vers tous les voisins j de i
        )
        for i in range(n)
    ]
    
    # Pour chaque arête (s, t) dans la liste st
    for s, t in st:
        # Si le sommet d'origine (s-1) a au moins un voisin
        if g[s-1]:
            # l est le nombre de voisins du sommet s-1
            l = len(g[s-1])
            # Si ce sommet a plus d'un voisin (l > 1), on considère la possibilité d'enlever l'arête
            if l > 1:
                # Calcul d'une candidate pour la réponse en tenant compte du retrait d'une arête sortante spécifique,
                # en recalculant l'espérance dans ce cas et en mettant à jour ans si on trouve mieux.
                ans = min(
                    allE + tf[s-1]*(1/(l-1) - 1/l) - toP[s-1]*(toE[s-1]+1+fromE[t-1])/(l-1),
                    ans
                )
    # On affiche la réponse finale, qui est l'espérance minimale trouvée
    print(ans)

# Appel de la fonction principale pour exécuter le programme lors de l'exécution du script
main()