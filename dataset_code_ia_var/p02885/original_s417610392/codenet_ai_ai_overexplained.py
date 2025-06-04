def main():
    # Demander à l'utilisateur de saisir deux nombres entiers séparés par un espace sur une seule ligne
    # La fonction input() lit la ligne entrée par l'utilisateur au clavier sous forme de chaîne de caractères
    # Par exemple, l'utilisateur peut entrer : 5 2
    utiles = input()
    # La méthode split() va couper la chaîne 'utiles' en séparant selon les espaces et retourne une liste des sous-chaînes
    # Donc '5 2' devient ['5', '2']
    morceaux = utiles.split()
    # La fonction map() applique la fonction int à chaque élément de la liste 'morceaux'
    # Cela transforme chaque sous-chaîne de chiffres en un entier
    # La liste ['5', '2'] devient [5, 2]
    valeurs = map(int, morceaux)
    # On utilise un "unpacking" (dépaquetage) pour assigner successivement les deux valeurs entières respectivement aux variables 'a' et 'b'
    a, b = valeurs

    # On veut calculer la valeur de 'a' moins le double de 'b', c'est-à-dire : a - b*2
    resultat = a - b * 2
    # Cependant, on ne veut pas que ce résultat soit négatif
    # La fonction max(0, resultat) compare 0 et 'resultat' puis retourne la plus grande des deux valeurs
    # Donc, si 'resultat' est négatif, 0 sera retourné ; sinon, 'resultat' sera retourné
    final = max(0, resultat)

    # On affiche la valeur finale calculée à l'utilisateur
    print(final)

# Cette condition spéciale vérifie si ce fichier est exécuté directement par l'utilisateur
# '__name__' est une variable spéciale qui vaut '__main__' si ce fichier est le programme principal
# Si c'est le cas, on appelle la fonction main() pour démarrer l'exécution du programme
if __name__ == '__main__':
    main()