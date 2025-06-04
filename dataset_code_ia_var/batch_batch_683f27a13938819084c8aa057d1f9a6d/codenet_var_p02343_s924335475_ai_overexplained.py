class UnionFind:
    # Le constructeur de la classe UnionFind accepte un entier n,
    # qui représente le nombre d'éléments. Cela initialise la structure.
    def __init__(self, n):
        # self.par est une liste où chaque position i (pour 0 <= i <= n)
        # contient la valeur i au départ, ce qui signifie que chaque élément
        # est son propre parent, donc chaque ensemble ne contient qu'un seul élément.
        # range(n+1) car on veut que les indices aillent de 0 jusqu'à n inclus.
        self.par = [i for i in range(n+1)]

        # self.rank est une liste qui garde trace de la "profondeur" (ou approximation)
        # de chaque arbre. Elle est initialisée à 0 pour chaque élément.
        self.rank = [0] * (n+1)

    # Méthode pour retrouver le représentant (la racine) de l'ensemble contenant x.
    # Cela utilise un algorithme appelé "chemin compressé" (path compression)
    # pour accélérer les recherches futures.
    def find(self, x):
        # Si le parent de x (self.par[x]) est lui-même, alors x est la racine.
        if self.par[x] == x:
            # On retourne x parce que c'est un leader/racine de son ensemble.
            return x
        else:
            # Si le parent de x n'est pas x, cela signifie qu'on doit continuer à parcourir
            # la structure jusqu'à trouver la vraie racine. On appelle find récursivement.
            # Cette ligne met aussi à jour le parent de x pour pointer directement vers la racine,
            # ce qui rendra les futures recherches plus rapides. C'est le "path compression".
            self.par[x] = self.find(self.par[x])
            # Retourne la racine trouvée pour x.
            return self.par[x]

    # Méthode pour unir les ensembles contenant x et y.
    # Cela fait cela de manière efficace en utilisant la "union by rank" pour
    # garder les arbres aussi plats que possible.
    def union(self, x, y):
        # On cherche la racine (le représentant) de l'ensemble qui contient x.
        x = self.find(x)
        # On cherche la racine de l'ensemble qui contient y.
        y = self.find(y)
        # Si la "profondeur" (rank) de l'arbre contenant x est PLUS PETITE que
        # celle de y, alors on rattache x sous y pour éviter de trop grandir l'arbre.
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            # Sinon, on raccroche y sous x (ou on les rattache au hasard si égalité).
            self.par[y] = x
            # Si les deux avaient le même rang, le nouveau chef (x) voit son rang augmenter de 1.
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # Méthode pour vérifier si x et y sont dans le même ensemble (même composante connexe).
    def same_check(self, x, y):
        # On utilise find pour chacun, et vérifie si la racine de x est la même que celle de y.
        return self.find(x) == self.find(y)

# Ce bloc s'exécute uniquement si le script est lancé directement (et non importé comme module).
if __name__ == "__main__":

    # On lit deux entiers séparés par un espace à l'entrée utilisateur :
    # n : nombre d'éléments   q : nombre de requêtes
    n, q = map(int, input().split())

    # On crée une instance de notre UnionFind pour n éléments (numérotés de 0 à n).
    u = UnionFind(n)

    # Liste pour stocker les réponses à certaines requêtes.
    ans_list = []

    # On répète q fois pour traiter chaque requête.
    for _ in range(q):
        # On lit trois entiers pour chaque requête :
        # com : le type de commande (1 ou autre)
        # x et y : les deux éléments concernés par la requête
        com, x, y = map(int, input().split())

        # Si com vaut 1, on doit vérifier si x et y sont dans le même ensemble.
        if com == 1:
            ans = u.same_check(x, y)  # sera True ou False
            ans_list.append(ans)      # on stocke la réponse dans la liste
        else:
            # Sinon (pour tout autre valeur de com), il faut unir les ensembles de x et y.
            u.union(x, y)

    # À la fin, pour toutes les requêtes "same_check", on affiche leur résultat.
    # int(True) donne 1, int(False) donne 0, donc on affiche 1 pour "OUI" et 0 pour "NON".
    for num in ans_list:
        print(int(num))