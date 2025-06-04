# Demander à l'utilisateur de saisir un nombre entier via le clavier
# La fonction input() affiche une invite à l'utilisateur et récupère ce qu'il saisit au clavier sous forme de chaîne de caractères (str)
# La fonction int() convertit cette chaîne de caractères en un entier (int)
x = int(input())

# Définition d'une fonction nommée 'f' qui prend un paramètre nommé 'x'
def f(x):
    # Vérification conditionnelle : si la valeur passée à 'x' est exactement égale à 1
    if x == 1:
        # Si condition vraie : retourner la valeur entière 7
        return 7
    else:
        # Si condition fausse : appel récursif à la fonction 'f' en décrémentant la valeur de 'x' de 1 (soit x-1)
        # La fonction multiplie ensuite le résultat de cet appel par 2, puis y ajoute 1
        # Ce processus répète la fonction jusqu'à ce que x atteigne la valeur de 1 (cas de base)
        return f(x-1) * 2 + 1

# Appel de la fonction 'f' avec la valeur entrée précédemment par l'utilisateur, puis on soustrait 1 au résultat obtenu
# L'opération 'f(x) - 1' calcule la valeur finale qui sera stockée dans la variable 'ans'
ans = f(x) - 1

# Affichage de la variable 'ans' à l'écran, ce qui montre le résultat final à l'utilisateur
print(ans)