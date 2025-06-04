# Demande à l'utilisateur de saisir une chaîne de caractères via le clavier
# La fonction input() affiche une invite (vide ici) et attend que l'utilisateur tape un texte suivi d'une pression sur "Entrée"
# La valeur entrée par l'utilisateur est récupérée sous forme de chaîne de caractères (type str) et stockée dans la variable s
s = input()

# Affiche certains caractères de la chaîne d'origine selon un pas précis d'indexation
# s[::2] est une notation de découpage appelée "slicing" sur les chaînes en Python
# La syntaxe générale est s[start:stop:step]
# - start : index de début (par défaut None, donc le premier caractère)
# - stop  : index de fin (par défaut None, donc jusqu'à la fin de la chaîne)
# - step  : intervalle entre chaque caractère sélectionné (ici, 2)
# s[::2] signifie : prendre chaque second caractère, en partant du premier, jusqu'à la fin
# Par exemple, si s vaut "Bonjour", alors s[::2] donnera "Bnojr"
# print() affiche sur la sortie standard (l'écran) la chaîne obtenue
print(s[::2])