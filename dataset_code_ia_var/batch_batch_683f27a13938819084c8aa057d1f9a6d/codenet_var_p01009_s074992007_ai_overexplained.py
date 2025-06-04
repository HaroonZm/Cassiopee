import sys

# Python augmente la limite de récursion pour éviter une erreur de dépassement de profondeur lors de l'exécution de récursion profonde.
# Ici, la limite est poussée à 10^9, ce qui est extrêmement élevé, afin d'être sûr que la récursion ne s'arrête pas prématurément.
sys.setrecursionlimit(10**9)

# Pour lire une ligne de l'entrée standard. L'utilisation de sys.stdin.readline() est préférée à input() pour des questions de performances quand il y a beaucoup de données à lire.
# 'input' devient donc une fonction qui renvoie la prochaine ligne lue sur l'entrée standard, sans le caractère de fin de ligne.
input = sys.stdin.readline

# Classe permettant de gérer une structure Union-Find (aussi connue sous le nom de Disjoint Set Union), ici pondérée, c'est-à-dire qu'en plus de l'ensemble des identifiants,
# elle maintient pour chaque élément une information de poids relatif aux opérations.
class WeightedUnionFind:
    # Constructeur de la classe : cette fonction s'appelle lorsqu'un objet de la classe est créé.
    def __init__(self, n):
        # On crée un tableau 'par' où l’indice i représente un élément, et la valeur stockée à par[i] est le parent de l’élément i dans l’arbre Union-Find.
        # Initialement, chaque élément est son propre parent.
        self.par = [i for i in range(n+1)]
        # 'rank' est un tableau qui stocke la profondeur approximative de l’arbre de chaque racine d’ensemble. Il aide à équilibrer l’arbre lors des unions pour optimiser les opérations.
        self.rank = [0] * (n+1)
        # 'weight' est un tableau qui stocke le poids total depuis chaque nœud jusqu’à la racine de son ensemble.
        self.weight = [0] * (n+1)
        # 'added' est utilisé pour faciliter le calcul des différences pondérées additionnelles entre éléments ; initialisé à 0 pour chaque élément.
        self.added = [0]*(n+1)

    # Méthode find : retrouve le représentant (racine) d’un élément x.
    def find(self, x):
        # Si x est son propre parent, cela signifie qu’il est la racine de son ensemble ; on le retourne.
        if self.par[x] == x:
            return x
        else:
            # Sinon, on cherche récursivement la racine de son parent.
            y = self.find(self.par[x])
            # En remontant, on accumule les poids du chemin parcouru pour maintenir l’invariant des poids à jour.
            # On ajoute le poids de par[x] à celui de x pour obtenir le poids total de x jusqu’à la racine.
            self.weight[x] += self.weight[self.par[x]]
            # On réalise le "chemin compressé" : on raccourcit véritablement le chemin en rattachant x directement à la racine trouvée.
            self.par[x] = y
            return y

    # Méthode union : fusionne les ensembles de x et y, en tenant compte d’un décalage pondéré w entre les deux.
    def union(self, x, y, w):
        # On trouve la racine (représentant) de x et y grâce à find.
        rx = self.find(x)
        ry = self.find(y)
        # On ajoute w aux valeurs 'added' respectives de x et y. Cela permet de garder une trace des ajustements de poids supplémentaires.
        self.added[x] += w
        self.added[y] += w
        # On compare les rangs (hauteurs approximatives des arbres pour les deux racines).
        # Si le rang de rx < rang de ry, on rattache l’arbre de rx à ry pour garder un arbre le plus équilibré possible.
        if self.rank[rx] < self.rank[ry]:
            # Le parent de rx devient ry.
            self.par[rx] = ry
            # On ajuste le poids de rx pour compenser correctement le passage de l’ensemble de rx sous ry.
            self.weight[rx] = w - self.diff(x, y)
        else:
            # Autrement, ry passe sous rx (arbre de ry devient enfant de rx). Cela inclut aussi le cas où les deux ensembles ont la même hauteur.
            self.par[ry] = rx
            self.weight[ry] = -w + self.diff(x, y)
            # Si les deux arbres avaient la même hauteur (rang), on augmente le rang de la "nouvelle" racine rx de 1 parce que sa hauteur augmente.
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    # Méthode same : permet de vérifier si x et y appartiennent au même ensemble (ont la même racine).
    def same(self, x, y):
        # Deux éléments sont dans le même ensemble si leur racine est la même.
        return self.find(x) == self.find(y)

    # Méthode diff : retourne la différence de poids entre x et y 
    # (totalement personnalisée ici avec la gestion de weight et added).
    def diff(self, x, y):
        # La différence de poids entre x et y s’obtient en soustrayant le poids de y de celui de x, tout en tenant compte des corrections avec 'added'.
        return self.weight[x] - self.weight[y]+self.added[x]-self.added[y]

    # Alias pour diff, pour plus de clarté ou d’extension future.
    def added_diff(self, x, y):
        return self.diff(x, y)

# Fonction qui gère l’instruction "IN" sur un triplet (a, b, c) reçu.
# Cela déclenche la fusion des ensembles de b et a avec la contrainte pondérée c.
def dealIn(l):
    a, b, c = l
    Un.union(b, a, c)

# Fonction qui gère l’instruction "OUT" ou autre test de différence.
# Elle retourne la différence pondérée si les éléments comparés sont dans le même ensemble,
# ou le message "WARNING" si ce n’est pas le cas.
def compare(l):
    a, b = l
    if Un.same(a, b):
        diff = Un.added_diff(b, a)
        return diff
    else:
        return "WARNING"

# Lecture du nombre N d’éléments et du nombre Q de requêtes à exécuter. Les valeurs sont extraites grâce à input() puis converties en entiers.
N, Q = map(int, input().split())
# Création de l’objet Union-Find pondéré pour N+1 éléments (on indexe de 0 à N).
Un = WeightedUnionFind(N+1)
# La liste des réponses à afficher à la fin, après traitement des Q requêtes.
ans = []
# La boucle traite chacune des Q requêtes :
for _ in range(Q):
    # On lit une ligne, on la découpe en éléments (espace-séparés). Le premier élément indique l’opération à effectuer.
    s, *l = input().split()
    if s == "IN":
        # Si c’est "IN", on interprète l’instruction et on la transmet à dealIn.
        dealIn(list(map(int, l)))
    else:
        # Sinon, on traite la comparaison et on collecte le résultat dans ans.
        ret = compare(list(map(int, l)))
        ans.append(ret)
# Si la liste des réponses contienne des éléments, on les affiche un par ligne.
if ans:
    print("\n".join(map(str, ans)))