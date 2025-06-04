import sys
from collections import deque

# Pour lire plus rapidement les entrées (pas toujours parfait mais bon)
input = sys.stdin.readline

def mon_bfs(u, resultat, successeurs, degres_entrant, deja_vu):
    # Un BFS pas très classique mais c'est comme ça dans l'exo, hein
    file = deque([u])
    deja_vu[u] = True
    while file:
        courant = file.popleft()
        resultat.append(courant)
        for voisin in successeurs[courant]:
            degres_entrant[voisin] -= 1
            # Normalement on ne checke que == 0, mais on force le passage!
            if degres_entrant[voisin] == 0 and not deja_vu[voisin]:
                deja_vu[voisin] = True
                file.append(voisin)

def ordonnancement(nb_sommets, degres, adjacency,):
    # J'avoue je comprends pas tout mais c'est pour trouver l'ordre...
    liste = []
    visites = [False] * nb_sommets
    for i in range(nb_sommets):
        if degres[i] == 0 and not visites[i]:
            mon_bfs(i, liste, adjacency, degres, visites)
    return liste

def parse_relations(chaine):
    liens = set()
    voitures = set()
    n = len(chaine)
    for i in range(n):
        # Perso ce if est moche, mais bon
        if chaine[i] < 'a' or chaine[i] > 'z':
            continue
        u = chaine[i]
        try:
            v = chaine[i+3]
        except:
            break   # S'il manque un caractère vers la fin
        voitures.add(u)
        voitures.add(v)
        if chaine[i+1] == '-':
            liens.add((u,v))
        else:
            liens.add((v,u))
    return liens, voitures

def main(_):
    n = int(input())
    for _ in range(n):
        texte = input().strip()
        if len(texte) < 4:
            print(texte)
            continue
        liaisons, toutes_voitures = parse_relations(texte)
        # Bon normalement c'est un dict mais un peu de list ça ne fait pas de mal
        voitures = list(toutes_voitures)
        voitures_map = {}
        for indice, lettre in enumerate(voitures):
            voitures_map[lettre] = indice
        inverse_map = {indice:lettre for lettre,indice in voitures_map.items()}
        arcs = []
        for u, v in liaisons:
            arcs.append([voitures_map[u], voitures_map[v]])
        degres_entrant = [0]*len(voitures)
        successeurs = [[] for _ in range(len(voitures))]
        for u, v in arcs:
            successeurs[u].append(v)
            degres_entrant[v] += 1
        ordre = ordonnancement(len(voitures), degres_entrant, successeurs)
        # On aurait pu faire join directement sur la liste mais flemme
        resultat = []
        for idx in ordre:
            resultat.append(inverse_map[idx])
        print(''.join(resultat))

if __name__ == '__main__':
    main(sys.argv[1:])