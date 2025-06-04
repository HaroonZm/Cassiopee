def solve():
    # Importation du module sys pour avoir accès à stdin (entrée standard).
    import sys
    # On alias la fonction readline pour lire plus rapidement les entrées ligne par ligne, équivalent à input().
    input = sys.stdin.readline

    # Lecture de la première ligne de l'entrée, qui contient deux entiers séparés par un espace.
    # map(int, input().split()) convertit chaque élément séparé par un espace en un entier.
    N, M = map(int, input().split())  # N est le nombre de sommets, M le nombre d'arêtes du graphe.

    # Création d'une liste d'adjacence standard pour chaque sommet : adjL.
    # La compréhension de liste [ [] for _ in range(N) ] crée une liste contenant N listes vides.
    adjL = [[] for _ in range(N)]  # Liste des voisins directs (arêtes sortantes) pour chaque sommet.
    adjLRev = [[] for _ in range(N)]  # Liste d'adjacence inversée : pour chaque sommet, ses prédécesseurs.
    outdegs = [0] * N  # Liste pour stocker le degré sortant (nombre d'arêtes sortantes) de chaque sommet, initialisé à 0.

    # Boucle pour lire les M arêtes du graphe.
    for _ in range(M):  # Pour chaque arête :
        # On lit deux entiers s et t (origine -> destination).
        s, t = map(int, input().split())
        # Conversion pour passer d'une indexation 1-based (commence à 1) à 0-based (commence à 0, python standard).
        s, t = s-1, t-1
        # On ajoute le sommet t comme voisin du sommet s (arête sortante de s vers t).
        adjL[s].append(t)
        # Pour la liste d'adjacence inversée, on ajoute s comme prédécesseur de t.
        adjLRev[t].append(s)
        # On incrémente le nombre d'arêtes sortantes pour le sommet s.
        outdegs[s] += 1

    # Initialisation des tableaux de probabilités et d'espérances d'arriver à chaque sommet depuis le sommet de départ (0).
    probs = [0] * N  # probs[v] contiendra la probabilité actuelle d'arriver au sommet v.
    expes = [0] * N  # expes[v] contiendra l'espérance (le nombre moyen de pas pour atteindre v depuis le départ).
    probs[0] = 1  # Au début, la probabilité d'être sur le sommet de départ (0) est de 1 (certain).

    # On parcourt les sommets dans l'ordre croissant pour propager les probabilités et espérances aux voisins.
    for v in range(N):
        prob, expe, outdeg = probs[v], expes[v], outdegs[v]  # Récupération des valeurs courantes pour ce sommet.
        if prob != 0:  # S'il y a une chance non nulle d'être arrivé à ce sommet.
            # On calcule le nombre d'étapes moyen (espérance/ probabilité) pour arriver ici.
            num = expe / prob  # On évite la division par zéro car on a déjà verifié que prob != 0.
            # On propage aux voisins (successeurs du sommet v).
            for v2 in adjL[v]:
                # On augmente la probabilité d'arriver à v2 avec la probabilité divisé par le nombre de choix possibles (outdeg).
                probs[v2] += prob / outdeg
                # On met à jour l'espérance pour v2 : elle augmente du coût de venir de v à v2 (=num+1, car un pas supplémentaire) pondéré par la probabilité associée.
                expes[v2] += prob * (num+1) / outdeg

    # Initialisation des mêmes variables mais pour le graphe inversé (pour simuler le processus en sens inverse depuis l'arrivée).
    probRevs = [0] * N  # Probabilités inverses: partant du sommet d'arrivée vers les précédents.
    expeRevs = [0] * N  # Espérances inverses: nombre d'étapes moyen pour venir de l'arrivée à chaque sommet.
    probRevs[-1] = 1  # On part du dernier sommet (N-1), probabilité d'être là = 1.
    # On parcourt les sommets en ordre décroissant (sens inverse) pour propager l'information.
    for v in reversed(range(N)):
        prob, expe = probRevs[v], expeRevs[v]  # Valeurs courantes du sommet v en sens inverse.
        if prob != 0:  # On n'actualise que si la probabilité est non nulle.
            num = expe / prob
            # Pour tous les prédécesseurs v0 de v dans le graphe original (successeurs dans le graphe inversé).
            for v0 in adjLRev[v]:
                # Actualisation de leurs probabilités/espérances, même logique que plus haut, en utilisant le degré sortant de v0 (dans le graphe normal).
                probRevs[v0] += prob / outdegs[v0]
                expeRevs[v0] += prob * (num+1) / outdegs[v0]

    # La réponse initiale est simplement l'espérance d'arriver à N-1 à partir du sommet 0.
    ans = expes[-1]

    # On explore l'optimisation éventuelle : retirer une arête sortante d'un sommet (sauf arrivee) si cela diminue l'espérance.
    for vRem in range(N-1):  # On parcourt tous les sommets sauf le dernier (l'arrivée).
        if outdegs[vRem] == 1:
            # Si le sommet n'a qu'une seule arête sortante, l'enlever le déconnecterait, donc on continue.
            continue
        values = []  # Liste pour stocker le "coût" associé à chaque arête sortante de vRem.
        prob, expe, outdeg = probs[vRem], expes[vRem], outdegs[vRem]  # On récupère les valeurs associées à vRem.
        for v2 in adjL[vRem]:  # Pour chaque voisin vers lequel vRem peut aller directement.
            # Calcul d'une valeur représentant la contribution de cette arête à l'espérance totale, en tenant compte des probabilités directes et inverses.
            value = expe*probRevs[v2] + expeRevs[v2]*prob + prob*probRevs[v2]
            values.append(value)
        sumV = sum(values)  # Somme de toutes les contributions des arêtes sortantes de vRem.
        # Calcul d'une espérance modifiée : on retire la moyenne des valeurs des arêtes sortantes.
        ans2 = expes[-1] - sumV / outdeg
        for value in values:  # Pour chaque arête potentiellement supprimée,
            # On calcule la nouvelle espérance si on enlève précisément cette arête (en recalcultant la moyenne sur outdeg-1 arêtes),
            # et on met à jour la réponse avec le minimum (on cherche l'optimisation maximale).
            ans = min(ans, ans2 + (sumV-value) / (outdeg-1))

    # Affichage de la réponse finale, c'est-à-dire la plus petite espérance trouvée.
    print(ans)

# Appel de la fonction principale qui effectue tous les calculs quand le script est exécuté.
solve()