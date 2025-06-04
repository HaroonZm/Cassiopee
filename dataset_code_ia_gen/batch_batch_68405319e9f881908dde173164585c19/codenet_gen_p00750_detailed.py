import sys
sys.setrecursionlimit(10**7)

# On va résoudre le problème par une recherche en profondeur mémorisée (DFS + memo),
# triant les transitions par ordre lexicographique pour s'assurer de trouver la plus
# lexicographiquement petite concaténation.
# Pour chaque nœud, on mémorise le résultat du chemin le plus puissant (lex. plus petit)
# vers le noeud gold.
# Deux cas d'impossibilité à retourner un chemin :
# - Pas de chemin du tout (retourner None)
# - Infinité de chemins de plus en plus petits lexicographiquement (cycle
#   qui permet de produire à l'infini un préfixe plus faible, détecté via un noeud
#   en cours de visite - "in recursion stack").
#
# On représente les arcs sous forme d’une liste d’adjacences avec (dest, label).
# On trie les arcs par label pour garantir que lors du DFS, on essaie d'abord les arcs
# menant à des chaînes lexicographiquement plus petites.
#
# Lors du DFS sur un noeud u:
# - on marque u comme en cours d'exploration
# - on explore tous ses arcs dans l'ordre lex.
# - pour chaque arc, on concatène label + résultat du noeud destination
# - on prend la plus petite chaîne lex. parmi celles obtenues
# - on marque u comme terminé (exploré)
#
# Si un cycle est détecté dans le chemin (un noeud en "en cours d'exploration")
# alors on retourne un état spécial "INFINITE" pour dire qu'on peut diminuer la chaîne
# indéfiniment => réponse "NO".
#
# A la fin, on affiche soit la chaîne minimale, soit "NO".

INFINITE = object()  # marqueur spécial pour cycle infini donnant plus puissant infini
NOCAN = None         # marqueur pour chemin impossible

def lex_min_concat(u, graph, g, state, memo):
    # state[u]: 0 = non visité, 1 = visite en cours (stack), 2 = visite terminé
    if state[u] == 1:
        # cycle détecté en cours d'exploration
        return INFINITE
    if state[u] == 2:
        # résultat déjà calculé
        return memo[u]

    if u == g:
        # si on est sur le noeud gold, chaîne vide (fin de chemin)
        state[u] = 2
        memo[u] = ""
        return ""

    state[u] = 1
    best = None  # None ou chaîne lex plus petite
    for v, lab in graph[u]:
        res = lex_min_concat(v, graph, g, state, memo)
        if res is INFINITE:
            # propagation cycle infini
            best = INFINITE
            break
        if res is not None:
            candidate = lab + res
            if best is None or candidate < best:
                best = candidate
    state[u] = 2
    memo[u] = best
    return best

def main():
    input = sys.stdin.readline
    while True:
        n, a, s, g = map(int, input().split())
        if n == 0 and a == 0 and s == 0 and g == 0:
            break

        graph = [[] for _ in range(n)]
        for _ in range(a):
            x, y, lab = input().split()
            x, y = int(x), int(y)
            graph[x].append((y, lab))
        # trier arcs par label lexicographique
        for u in range(n):
            graph[u].sort(key=lambda x: x[1])

        state = [0]*n
        memo = [None]*n

        result = lex_min_concat(s, graph, g, state, memo)

        if result is None or result is INFINITE:
            print("NO")
        else:
            print(result)

if __name__ == "__main__":
    main()