import sys

# La fonction sys.setrecursionlimit permet de définir la limite maximale de récursivité autorisée
# Python a une limite par défaut de profondeur d'appel récursif (souvent autour de 1000)
# Ici, on la modifie à 100000 pour permettre des appels récursifs très profonds
# Cela est nécessaire si la fonction visit() fait beaucoup d'appels récursifs
sys.setrecursionlimit(100000)

# Définition de la fonction principale main() qui sera le point d'entrée principal du script
def main():
    # Lecture de deux entiers séparés saisis par l'utilisateur, qui correspondent ici au nombre de sommets (V) et d'arêtes (E)
    # int(input()) convertit la chaîne de caractères obtenue en entier
    V, E = int(input()), int(input())
    
    # Initialisation d'une liste vide L, qui servira à stocker l'ordre de visite des sommets
    L = []
    # Pour optimiser l'accessibilité, on récupère une référence directe à la méthode append de L
    # Cela évite une recherche répétée de la méthode lors des appels app(x)
    app = L.append
    
    # Création d'une liste 'visited' de taille V où chaque élément vaut 0
    # Cette liste sert à marquer si un sommet a été visité ou non lors du parcours
    # 0 signifie non visité, 1 signifie visité
    visited = [0 for i in range(V)]
    
    # Création d'une liste d'adjacence 'edges', contenant V sous-listes vides
    # Chaque sous-liste correspond à un sommet et contiendra les sommets adjacents (les arêtes sortantes)
    edges = [[] for i in range(V)]
    
    # Définition d'une fonction récursive visit(x) pour parcourir les sommets en profondeur (DFS)
    def visit(x):
        # Si le sommet x n'a pas encore été visité (visited[x] == 0)
        if not visited[x]:
            # On marque le sommet comme visité
            visited[x] = 1
            # Pour chaque sommet e adjacent au sommet x
            for e in edges[x]:
                # On appelle récursivement la fonction visit(e) pour continuer le parcours en profondeur
                visit(e)
            # Après avoir visité tous les successeurs, on ajoute ce sommet x à la liste L
            # Cela assure que les sommets sont ajoutés dans un ordre où les dépendances sont respectées
            app(x)
    
    # Boucle de 0 jusqu'à E-1 pour lire les arêtes
    for i in range(E):
        # Lecture d'une ligne d'entrée contenant deux entiers correspondant à une arête d'un graphe dirigé
        # map(int, input().split()) lit cette ligne sépare les deux nombres et les convertit en entiers
        s, t = map(int, input().split())
        # L'arête est ajoutée dans la liste d'adjacence : sommet s-1 pointe vers sommet t-1
        # Les indices sont décalés de 1 car la numérotation entrée commence à 1 alors que l'indexation Python commence à 0
        edges[s - 1].append(t - 1)
    
    # Pour chaque sommet i dans l'intervalle 0 à V-1
    for i in range(V):
        # Si le sommet i n'a pas encore été visité
        if not visited[i]:
            # Appeler visit pour effectuer le DFS et remplir la liste L
            visit(i)
    
    # Une fois les appels récursifs terminés, L contient un ordre topologique inversé
    # On renverse donc la liste pour obtenir l'ordre topologique correct
    L.reverse()
    
    # Initialisation d'un drapeau flag à 0 (utilisé comme booléen)
    flag = 0
    
    # Parcours des sommets dans la liste L selon l'ordre topologique obtenu
    for i in range(V):
        # Affichage du sommet courant augmenté de 1 pour conserver la numérotation initiale
        print(L[i] + 1)
        # Condition pour vérifier s'il y a un saut dans l'ordre topologique :
        # - flag doit être encore 0 (non activé)
        # - on ne regarde pas le dernier sommet (car on regarde la suivante)
        # - on vérifie si le sommet suivant dans L n'est pas un successeur direct du sommet courant dans les arêtes
        # Si cette condition est vraie, cela signifie qu'il n'existe pas d'arête directe reliant L[i] à L[i+1],
        # donc le drapeau flag passe à 1 pour notifier qu'une arête est manquante dans l'ordre
        if not flag and i < V - 1 and (L[i + 1] not in edges[L[i]]):
            flag = 1
    
    # Impression finale de la valeur de flag
    # 0 signifie qu'à chaque étape il y avait une arête directe entre sommets consécutifs dans la liste ordonnée
    # 1 signifie qu'il y a au moins un saut, donc un lien direct manquant entre deux sommets successifs
    print(flag)

# Appel à la fonction main() pour lancer l'exécution du script
main()