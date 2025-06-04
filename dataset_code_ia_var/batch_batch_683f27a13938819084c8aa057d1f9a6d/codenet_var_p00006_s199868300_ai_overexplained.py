# Demande à l'utilisateur de saisir une entrée via le terminal/la console
# La fonction raw_input() affiche une invite (vide ici) à l'utilisateur et attend que celui-ci saisisse une chaîne de caractères suivie de la touche Entrée.
# La chaîne saisie est ensuite stockée dans la variable 'instr'.
instr = raw_input()

# Affiche la valeur de la variable 'instr', mais renversée (reversed).
# L'opérateur de tranchage [::-1] signifie :
#    - Le premier ':' indique qu'on souhaite prendre toute la chaîne (pas de borne de début ou de fin spécifiée)
#    - Le deuxième ':' suivi de -1 signifie qu'on prend chaque caractère en partant de la fin jusqu'au début (étape -1)
#    - Cela inverse l'ordre des caractères de la chaîne
# La fonction print affiche le résultat à l'écran (dans la console)
print instr[::-1]