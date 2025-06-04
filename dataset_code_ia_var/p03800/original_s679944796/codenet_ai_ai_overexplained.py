# Demande à l'utilisateur d'entrer un entier qui représentera le nombre total d'animaux
# La fonction input() retourne une chaîne de caractères, donc on la convertit en entier avec int()
n_ani = int(input())

# Demande à l'utilisateur d'entrer une chaîne de caractères représentant les réponses de chaque animal ("o" ou "x")
# Ensuite, on convertit cette chaîne en liste pour pouvoir accéder à chaque caractère facilement
l_ans = list(input())

# Définition d'une fonction qui détermine le prochain type d'animal à partir de l'animal précédent, de l'animal actuel, et de la réponse ('o' ou 'x')
def get_next_animal(pre_ani, now_ani, ans):
    # Si l'animal précédent est "S" (Sheep)
    if pre_ani == "S":
        # Si l'animal actuel est aussi "S"
        if now_ani == "S":
            # Si la réponse actuelle est "o" (identique au voisin précédent)
            if ans == "o":
                return "S"  # Le prochain animal est aussi "S"
            else:
                return "W"  # Sinon, le prochain animal est "W" (Wolf)
        else:
            # Si l'animal actuel est "W" (Wolf)
            if ans == "o":
                return "W"
            else:
                return "S"
    else:
        # Si l'animal précédent est "W" (Wolf)
        if now_ani == "S":
            if ans == "o":
                return "W"
            else:
                return "S"
        else:
            # Si l'animal précédent est "W" et l'animal actuel aussi
            if ans == "o":
                return "S"
            else:
                return "W"

# Fonction pour vérifier la validité d'une séquence pour une combinaison précise du premier et du dernier animal
def solve_question(first_ani, last_ani):
    # La liste globale l_ani va contenir la séquence d'animaux déterminée
    global l_ani
    # Ajoute le premier animal à la liste (par exemple "S" ou "W")
    l_ani.append(first_ani)
    # On déduit le deuxième animal à partir du "dernier" animal (qui précède le premier), du premier, et de la première réponse fournie
    next_ani = get_next_animal(last_ani, first_ani, l_ans[0])
    # Ajoute cet animal à la séquence
    l_ani.append(next_ani)
    # Utilise une boucle pour remplir la liste des animaux de la 3ème à la n-ième position
    # La boucle commence à 1 car on a déjà les deux premiers animaux
    for i in range(1, (n_ani - 1)):
        # Calcule le prochain animal en fonction des deux précédents et de la réponse à la position i
        next_ani = get_next_animal(l_ani[i - 1], l_ani[i], l_ans[i])
        # Ajoute le prochain animal à la liste globale
        l_ani.append(next_ani)
    # Après avoir généré la séquence, vérifier si les contraintes cycliques sont respectées
    # c'est-à-dire le dernier animal doit correspondre à last_ani, et le suivant du dernier doit boucler sur le premier
    # En utilisant la fonction get_next_animal avec les bons indices
    if l_ani[(n_ani - 1)] == last_ani and get_next_animal(l_ani[(n_ani - 2)], l_ani[(n_ani - 1)], l_ans[(n_ani - 1)]) == l_ani[0]:
        return "ok"  # La séquence est valide
    else:
        return "ng"  # La séquence ne respecte pas les contraintes

# Initialise un compteur pour suivre le nombre de solutions invalides essayées
ng_counter = 0

# On teste les 4 combinaisons possibles pour la première et la dernière position : ("S","S"), ("S","W"), ("W","S"), ("W","W")
# Ceci couvre toutes les hypothèses de départ (Sheep ou Wolf à chaque extrémité)
for i in range(4):
    # Liste qui va contenir la séquence générée pour cette hypothèse
    l_ani = []
    # Premier cas : les deux extrémités sont des moutons ("S")
    if i == 0:
        fir_ani = "S"
        las_ani = "S"
        # On essaie de voir si cette configuration donne une séquence valide
        if solve_question(fir_ani, las_ani) == "ok":
            # Si oui, on affiche la séquence complète, concaténée en une seule chaîne de caractères
            print("".join([i for i in l_ani]))
            break  # On arrête le programme, car on a trouvé une solution
        else:
            ng_counter += 1  # Sinon, on incrémente le compteur de tentatives infructueuses
    # Deuxième cas : premier animal "S", dernier animal "W"
    elif i == 1:
        fir_ani = "S"
        las_ani = "W"
        if solve_question(fir_ani, las_ani) == "ok":
            print("".join([i for i in l_ani]))
            break
        else:
            ng_counter += 1
    # Troisième cas : premier animal "W", dernier animal "S"
    elif i == 2:
        fir_ani = "W"
        las_ani = "S"
        if solve_question(fir_ani, las_ani) == "ok":
            print("".join([i for i in l_ani]))
            break
        else:
            ng_counter += 1
    # Quatrième cas : les deux extrémités sont des loups ("W")
    elif i == 3:
        fir_ani = "W"
        las_ani = "W"
        if solve_question(fir_ani, las_ani) == "ok":
            print("".join([i for i in l_ani]))
            break
        else:
            ng_counter += 1

# Si aucune des 4 combinaisons ne donne une séquence valide, on affiche -1 qui signifie "impossible"
if ng_counter == 4:
    print(-1)