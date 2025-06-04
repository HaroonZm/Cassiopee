import heapq  # Importe le module heapq pour utiliser une file de priorité (min-heap en Python)

# Déclaration d'une classe pour représenter chaque état d'un point dans la recherche
class point:
    # Le constructeur de la classe qui initialise un objet point
    def __init__(self, total, use, place):
        self.total = total   # Le coût total jusqu'à présent pour atteindre ce point (entier)
        self.use = use       # Le coût de la dernière transition ou "usage" (entier)
        self.place = place   # L'indice du point actuel (entier)

    # Définition de la comparaison pour utiliser les objets point dans un min-heap
    # La méthode __lt__ est la comparaison "inférieur à" (less than)
    def __lt__(self, other):
        # Priorité sur l'attribut 'total', et en cas d'égalité,
        # priorité sur 'use' (avec un critère personnalisé)
        # Ici, si les totaux sont égaux, on préfère celui qui a un 'use' plus petit
        return self.total < other.total or (self.total == other.total and self.use < other.use)

# Lecture de trois entiers à partir de l'entrée standard, séparés par des espaces
# w : largeur, h : hauteur, n : nombre de "lights"
w, h, n = map(int, input().split())

# Cas particulier où la grille fait 1x1, il n'y a rien à faire
if w == 1 and h == 1:
    print(0)   # Affiche 0 car aucune opération n'est nécessaire
    exit()     # Quitte le programme immédiatement

# Lecture des coordonnées des 'n' lumières, un tableau 2D pour stocker chaque light
lights = [list(map(int, input().split())) for _ in range(n)] 

que = []   # Initialisation d'une liste qui servira de file de priorité (min-heap)
mins = []  # Liste pour garder la meilleure valeur de chaque point (pour l'algorithme)

# On initialise la file de priorité et le tableau des valeurs minimales
for i, j in enumerate(lights):
    # La distance du point lumière à l'origine (1,1), on convertit les coordonnées en index
    dis = j[0] + j[1] - 2
    # On utilise un objet 'point' pour garder l'état
    heapq.heappush(que, point(dis, dis, i))  # On l'ajoute à la heap
    mins.append(point(dis, dis, i))          # On garde ce point comme la meilleure valeur connue

ans = 100000  # On initialise la réponse avec une valeur très grande (suppose que le résultat sera plus petit)

# Boucle principale tant que la file de priorité n'est pas vide
while que:
    # On prend l'élément de coût le plus faible actuel
    top = heapq.heappop(que)
    
    # On évalue si atteindre le coin opposé (w, h) à partir de cette lumière réduit la solution
    # On calcule la distance résiduelle pour joindre (w,h) depuis la lumière actuelle
    direct_move = abs(w - lights[top.place][0]) + abs(h - lights[top.place][1])  # Chemin direct restant
    # On calcule le coût d'ajouter ce chemin direct mais en tenant compte du "use" déjà utilisé
    ans = min(ans, top.total + max(0, direct_move - top.use))  # On ne fait rien si top.use couvre ce coût

    # On essaie de passer d'une lumière à une autre pour voir si on obtient un meilleur résultat
    for i in range(len(lights)):
        # La distance entre la lumière actuelle (top.place) et une nouvelle lumière (i)
        dis = abs(lights[top.place][0] - lights[i][0]) + abs(lights[top.place][1] - lights[i][1]) - 1
        # Si déjà couvert par use, on ne paie rien sinon il reste un coût positif
        use = max(0, dis - top.use)
        # Nouveau total en incluant ce déplacement
        total = top.total + use
        # Création du nouvel état
        new = point(total, use, i)
        # Si ce nouveau chemin jusqu'à 'i' est meilleur que le précédent, on met à jour
        if mins[i] > new:
            mins[i] = new              # On met à jour pour le prochain passage
            heapq.heappush(que, new)   # On ajoute l'état à traiter dans la file de priorité

print(ans)  # Après avoir tout examiné, on affiche la meilleure solution trouvée