# Lecture d'une valeur entière depuis l'entrée standard, représentant le nombre d'équipes
n = int(raw_input())  

# Initialisation d'un dictionnaire vide pour stocker les points de chaque équipe
dic = {}  

# Initialisation d'un autre dictionnaire pour stocker le classement (rang) final de chaque équipe
rank = {}  

# Variable compteur pour gérer les égalités lors du classement
count = 0  

# Variable pour suivre le rang courant lors du classement; initialisée à -1 car on va incrémenter avant usage
now_rank = -1  

# Variable pour mémoriser la valeur des points de l'équipe précédente lors du tri, initialisée à -1 pour garantir qu'elle diffère du premier score
prev = -1  

# Boucle pour initialiser à 0 les points pour chaque équipe avec leur index comme clé
for i in range(n):
    dic[i] = 0  

# Boucle sur le nombre de matchs possibles dans un tournoi à chaque équipe jouant contre chaque autre exactement une fois
# Ce nombre est n*(n-1)/2, selon la formule combinatoire du nombre de couples dans un ensemble de cardinal n
for i in range(n*(n-1)/2):  
    # Lecture d'une ligne contenant quatre entiers séparés par un espace:
    # a et b sont les indices des deux équipes, c et d leurs scores respectifs dans le match
    a, b, c, d = [int(i) for i in raw_input().split(" ")]  
    
    # Si l'équipe a a marqué plus de points que l'équipe b
    if c > d:  
        # Attribution de 3 points à l'équipe a (indexée à a-1 à cause du décalage entre nombre d'équipes et indices 0-based)
        dic[a-1] += 3  
    # Si l'équipe b a marqué plus de points que l'équipe a
    elif c < d:
        # Attribution de 3 points à l'équipe b
        dic[b-1] += 3  
    # Si les deux équipes ont fait match nul (score égal)
    else:  
        # Attribution d'1 point à chacune des deux équipes pour un match nul
        dic[a-1] += 1  
        dic[b-1] += 1  

# Création d'une liste des couples (équipe, points) à partir des paires clés-valeurs du dictionnaire dic
l = dic.items()  

# Tri de la liste pour ordonner les équipes par leurs points de manière décroissante
# cmp est une fonction de comparaison définie par lambda qui compare les points de deux équipes x et y et ordonne du plus grand au plus petit
l.sort(cmp=(lambda x,y: cmp(y[1], x[1])))  

# Parcours de la liste triée pour attribuer un rang à chaque équipe en prenant en compte les égalités de points
for i in range(len(l)):
    # Si le nombre de points de l'équipe courante est égal à celui de l'équipe précédente
    if prev == l[i][1]:
        # On incrémente le compteur pour enregistrer le nombre d'équipes ex æquo
        count += 1  
    else :
        # Sinon, on met à jour le rang courant en sautant le nombre d'équipe ex æquo + 1
        now_rank += count + 1  
        # On met à jour la variable prev avec la valeur des points de l'équipe courante pour les prochaines comparaisons
        prev = l[i][1]  
        # Réinitialisation du compteur à 0 pour une nouvelle série de scores différents
        count = 0  

    # Mise à jour du dictionnaire rank où la clé est l'index de l'équipe et la valeur est le rang calculé (ajusté de +1 car le rang commence à 1)
    rank.update({l[i][0]:now_rank+1})  

# Boucle finale qui affiche pour chaque équipe (dans l'ordre des indices de 0 à n-1) son rang calculé
for i in range(n):
    print rank[i]