# Demande une entrée utilisateur via la fonction input(). La valeur saisie est une chaîne de caractères, qui sera affectée à la variable s.
s = input()

# La fonction print() sert à afficher le résultat sur la console.
print(
    # On effectue l'opération suivante : 
    # (s[0] == 'A') + sum(s[i] >= s[i+1] for i in range(len(s)-1))
    #
    # 1. s[0] == 'A' :
    #    - s[0] représente le premier caractère de la chaîne s (indice 0, car l'indexation commence à 0 en Python).
    #    - '==' est l'opérateur de comparaison d'égalité. Il renvoie True si la valeur de gauche est égale à celle de droite, sinon False.
    #    - 'A' est le caractère à comparer.
    #    - Le résultat de cette comparaison sera un booléen (True ou False).
    #    - En contexte arithmétique, True vaut 1 et False vaut 0, donc on obtient 1 si le premier caractère est 'A', 0 sinon.
    (s[0] == 'A') +
    # 2. sum(s[i] >= s[i+1] for i in range(len(s)-1)) :
    #    - On utilise la fonction sum(), qui additionne tous les éléments d'un itérable (dans ce cas, un générateur).
    #    - Le générateur s[i] >= s[i+1] for i in range(len(s)-1) produit une séquence de valeurs True ou False.
    #      a. range(len(s)-1) :
    #         - len(s) donne la longueur de la chaîne s.
    #         - range(len(s)-1) génère une séquence de nombres entiers de 0 à len(s)-2 inclus (donc, chaque indice i allant du début jusqu'à l'avant-dernier caractère de s).
    #         - Cela permet de comparer chaque caractère s[i] avec son successeur s[i+1].
    #      b. s[i] >= s[i+1] :
    #         - À chaque itération, on compare le caractère à l'indice i avec celui à l'indice i+1.
    #         - '>=' est l'opérateur de comparaison "supérieur ou égal à".
    #         - Cette comparaison donne True si la condition est remplie, sinon False.
    #      c. Pour chaque i, le résultat (True ou False) est "consommé" par sum(), qui additionne chaque True en tant que 1, et chaque False en tant que 0.
    #      d. Cela donne le nombre de fois où un caractère est supérieur ou égal à son voisin de droite dans la chaîne initiale.
    sum(
        s[i] >= s[i+1]   # Expression booléenne : compare si le caractère actuel est supérieur ou égal au suivant.
        for i in range(len(s)-1)   # Générateur parcourant les indices de 0 à len(s)-2 pour éviter l'IndexError.
    )
)
# Ainsi, le programme affiche la somme :
# - de 1 si le premier caractère est 'A' (sinon 0)
# - et du nombre de paires de caractères consécutifs dans s où le caractère de gauche est >= celui de droite.