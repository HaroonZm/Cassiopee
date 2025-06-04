# Définition de la fonction Bellman-Ford qui va nous permettre de trouver le chemin le plus court
def bellman_ford(graph, source):
    # On crée une liste pour stocker les plus courts chemins vers chaque sommet.
    # 'd' va contenir la "distance" minimale depuis la source vers tous les sommets au départ.
    # On l'initialise avec INF (une valeur représentant l'infini, c'est-à-dire, inatteignable).
    d = [INF] * n

    # On indique que la distance du sommet de départ (source 'g') à lui-même est de longueur 0.
    # Ici, par convention particulière, on assigne une chaîne vide '' comme "distance 0"
    d[g] = ''

    # On va faire au maximum n*6+1 tours d'itérations (adaptation du nombre d'itérations, 
    # normalement Bellman-Ford utilise n-1 mais ici on veut éviter les cycles).
    for i in range(n * 6 + 1):
        # On utilise une variable qui va nous indiquer si au moins une mise à jour a eu lieu pendant cette passe
        update = False
        # Parcours de toutes les arêtes du graphe (chaque arête est un triplet (départ, arrivée, poids))
        for e in graph:
            # On vérifie si on connaît un chemin jusqu'au sommet d'arrivée (e[1]) (ce n'est donc pas INF)
            # et si aller de l'arrivée vers le départ, en utilisant l'arête e, donne une distance plus courte.
            if d[e[1]] != INF and d[e[0]] > e[2] + d[e[1]]:
                # Si c'est le cas, on met à jour la distance minimale vers ce sommet.
                d[e[0]] = e[2] + d[e[1]]
                # Puisque mise à jour, on note la modification
                update = True
        # On vérifie si la "distance" vers le sommet but (s) dépasse une certaine taille, indiquant un cycle.
        if len(d[s]) > n * 6:
            # On retourne None pour indiquer un cycle ou un problème.
            return None
        # Si aucune modification n’a été faite lors de cette passe, alors toutes les distances minimales sont trouvées
        if not update:
            # On retourne la chaîne minimale trouvée jusqu'à 's' (sommet destination)
            return d[s]
    else:
        # Si on a fini toutes les itérations sans "early exit", on retourne aussi la chaîne trouvée.
        return d[s]

# On définit INF comme une accolade ouvrante '{'
# Cette valeur est choisie car, en tri lexical (ordre ASCII), toute lettre minuscule 
# ou majuscule vient avant '{', donc '{' est "plus grand" que n'importe quelle chaîne
INF = '{'

# Boucle principale de lecture des jeux de données
while True:
    # On lit une ligne d'entrée, on la découpe en morceaux, on convertit chaque morceau en entier,
    # et on les affecte respectivement à n, a, s, g :
    # n : nombre de sommets
    # a : nombre d'arêtes
    # s : sommet destination (numéroté de 0 à n-1)
    # g : sommet de départ (numéroté de 0 à n-1)
    n, a, s, g = (int(s) for s in input().split())
    # Si tous les paramètres valent zéro, c'est la condition d'arrêt (fin de jeu de données)
    if (n, a, s, g) == (0, 0, 0, 0):
        break

    # On définit quelques listes (ici 'flag' et 'edge' sont inutilisées dans la suite du code)
    flag = []
    edge = []
    # Cette liste va stocker les arêtes du graphe
    es = []
    # Pour chaque arête à lire (le nombre d'arêtes 'a' est donné), on lit chaque ligne,
    # on sépare la ligne en 3 morceaux (xs, ys, labi) : extrémité de départ, d'arrivée, et l'étiquette/poids
    for i in range(a):
        xs, ys, labi = input().split()
        # On ajoute à la liste 'es' un tuple de (extrémité départ as int, extrémité arrivée as int, étiquette/poids)
        es.append((int(xs), int(ys), labi))

    # On appelle la fonction bellman_ford pour trouver le plus court chemin lexicalement parlant
    spell = bellman_ford(es, g)

    # Si la réponse n'est atteignable (toujours INF ou None, ce qui signifie soit pas de chemin, soit cycle négatif)
    if spell == INF or spell is None:
        # On affiche NO ("non atteignable" ou "impossible")
        print('NO')
    else:
        # Sinon, on affiche la chaîne minimale trouvée
        print(spell)