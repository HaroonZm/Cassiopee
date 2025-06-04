# Demander une entrée à l'utilisateur pour 'n', qui sera le nombre dont nous allons analyser les chiffres.
# On convertit l'entrée en string (chaîne de caractères) pour pouvoir accéder à ses chiffres individuellement.
n = str(input())

# Demander une entrée à l'utilisateur pour 'p', qui représentera le nombre de chiffres "non zéros" à considérer.
# On convertit cette entrée en un entier avec int(), car on fera des opérations mathématiques dessus.
p = int(input())

# Calculer le nombre total de chiffres dans la chaîne 'n' à l'aide de la fonction len().
# keta contiendra donc la longueur de 'n'.
keta = len(n)

# Initialiser la variable 'Dp' qui sera notre tableau de programmation dynamique (DP).
# C'est une liste 3D (trois dimensions) :
#   Dp[i][j][bound]
#   i : indice du chiffre actuel que nous traitons (0 à keta)
#   j : nombre de chiffres non-zéros utilisés jusqu'ici (0 à keta)
#   bound (0 ou 1) : 
#       1 signifie que l'on est encore "à la limite" de 'n' (c'est-à-dire les chiffres n'ont jamais dépassé n),
#       0 signifie qu'on a déjà pris une valeur plus petite donc on peut choisir n'importe quel chiffre de 0 à 9 librement.
# À chaque niveau, on initialise la valeur à 0, car au départ, il n'existe aucun nombre construit.
Dp = [[[0 for _ in range(2)] for _ in range(keta+1)]for _ in range(keta+1)]

# On initialise le point de départ :
# Dp[0][0][1] = 1 veut dire : il existe exactement 1 façon de ne rien avoir choisi,
# zéro chiffre non-zéro utilisé, et on est (par défaut) à la borne (bound == 1) 
Dp[0][0][1] = 1

# La boucle principale traite chaque chiffre de la gauche vers la droite.
# 'i' : correspond au chiffre sur lequel on se trouve (de 0 jusqu'à keta-1, car range(keta) exclut keta)
for i in range(keta):
    # 'j' : nombre de chiffres non-zéro utilisés jusqu'à présent (de 0 à i inclus)
    for j in range(i+1):
        # On va essayer tous les chiffres possibles (de 0 à 9 inclus) pour cette position.
        for k in range(10):
            # Comme le DP distingue entre les transitions qui sont encore sur la limite de n ou pas,
            # on doit séparer le cas k==0 (on place un 0) du cas k!=0 (on place un chiffre non-zéro)
            if k == 0:
                # Si on place un 0 à cette position :
                # Premier cas : tant qu'on n'a pas dépassé la valeur de n,
                # donc si k < int(n[i]), alors on passe dans zone libre (bound 0)
                if k < int(n[i]):
                    #     - On ajoute tous les cas où on était déjà en zone libre (bound 0)
                    Dp[i+1][j][0] += Dp[i][j][0]
                    #     - On ajoute aussi tous les cas où on était encore à la limite (bound 1)
                    Dp[i+1][j][0] += Dp[i][j][1]
                # Deuxième cas : si k égal au chiffre de n à la position i, on reste sur la "limite"
                elif k == int(n[i]):
                    # On ajoute les façons où on continue à suivre la limite (bound 1)
                    Dp[i+1][j][1] += Dp[i][j][1]
                    # Mais si on était déjà libéré de la borne (bound 0), on continue simplement.
                    Dp[i+1][j][0] += Dp[i][j][0]
                # Troisième cas : k > n[i]; impossible si on est encore sur la borne, mais on peut continuer en bound 0
                else:
                    Dp[i+1][j][0] += Dp[i][j][0]
            else:
                # Si on place un chiffre non-zéro à cette position :
                if k < int(n[i]):
                    # On tombe dans la zone "libre" à partir de maintenant (bound 0)
                    # Pour chaque solution, on incrémente le nombre de chiffres non-zéro utilisés (j+1)
                    Dp[i+1][j+1][0] += Dp[i][j][0]
                    Dp[i+1][j+1][0] += Dp[i][j][1]
                elif k == int(n[i]):
                    # On reste à la borne (bound 1) dans les cas où on était encore lié à la limite ("tight")
                    Dp[i+1][j+1][1] += Dp[i][j][1]
                    # Mais on peut aussi continuer en zone libre (bound 0)
                    Dp[i+1][j+1][0] += Dp[i][j][0]
                else:
                    # k > n[i] : seulement possible en bound 0
                    Dp[i+1][j+1][0] += Dp[i][j][0]

# Après avoir traité tous les chiffres, il ne reste plus qu'à donner la réponse selon la contrainte sur le nombre de chiffres non-zéro.
# Si p, le nombre de chiffres non-zéros à utiliser, est plus grand que le nombre total de chiffres, il ne peut pas y avoir de nombre de ce type.
if p > keta:
    print(0)
else:
    # Sinon, la réponse est la somme des deux états (borne respectée et borne dépassée) pour le dernier chiffre et p chiffres non-zéro
    print(sum(Dp[-1][p]))