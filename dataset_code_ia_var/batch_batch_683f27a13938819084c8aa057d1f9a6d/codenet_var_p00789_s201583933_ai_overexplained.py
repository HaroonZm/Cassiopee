# Crée une liste nommée 'dp' contenant 301 éléments, chacun initialisé à la valeur 1
# 'dp' servira à stocker le nombre de façons d'exprimer chaque entier de 0 à 300
# comme somme d'entiers qui sont des carrés parfaits (comme 1, 4, 9, 16, ...)
dp = [1] * 301

# Boucle 'for' qui parcourt les entiers de 2 jusqu'à 17 inclus (range(2, 18))
# Cela correspond à utiliser les carrés parfaits de 2*2 (4) à 17*17 (289)
for i in range(2, 18):
    # Pour chaque carré parfait i*i, on va parcourir tous les entiers j allant de i*i jusqu'à 300 inclus
    # Cela permet de voir quelles sommes peuvent être formées en ajoutant ce carré parfait
    for j in range(i * i, 301):
        # Pour l'entier j, on ajoute au nombre de façons déjà comptabilisées (dp[j])
        # le nombre de façons d'écrire (j - i*i) comme somme de carrés parfaits
        # Ainsi, on construit la solution pour chaque nombre à partir des plus petits 
        # vers les plus grands, en tenant compte de l'ajout de chaque nouveau carré parfait comme terme
        dp[j] += dp[j - i * i]

# Boucle infinie qui permettra de traiter plusieurs entrées utilisateur
while 1:
    # Lit une entrée au clavier attendue, la convertit en entier, et la stocke dans la variable n
    n = int(input())
    # Si l'utilisateur entre 0, on quitte la boucle (cela termine le programme)
    if n == 0:
        break
    # Affiche la valeur dp[n], c'est-à-dire le nombre de façons d'exprimer n comme somme de carrés parfaits
    print(dp[n])