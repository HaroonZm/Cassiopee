import sys  # Importe le module sys, qui fournit des fonctions et objets liés à l'environnement d'exécution du système, comme l'accès à stdin (entrée standard)

def main():  # Définit une fonction nommée 'main' qui encapsule la logique principale du programme
    m = []  # Crée une liste vide nommée 'm' qui servira à stocker des nombres convertis en float ; ici, le commentaire indique que m signifie "mountain"

    # La boucle suivante va lire chaque ligne de l'entrée standard (sys.stdin)
    # sys.stdin est un flux représentant l'entrée standard, habituellement le clavier ou la redirection d'un fichier
    for line in sys.stdin:  # Pour chaque 'line' (chaîne de caractères terminée par un saut de ligne) lue depuis sys.stdin
        # La ligne qui vient d'être lue depuis l'entrée standard (string) est convertie en nombre à virgule flottante (float)
        # Cela suppose que chaque ligne représente un nombre valide au format texte
        # L'appel à float(line) enlève les espaces inutiles et convertit la chaîne en un nombre flottant Python
        m.append(float(line))  # On ajoute le nombre converti à la liste 'm' grâce à la méthode 'append' qui insère un élément à la fin de la liste

    # Après avoir collecté tous les nombres, il faut les organiser dans l'ordre croissant
    # On appelle la méthode sort() qui trie la liste 'm' sur place (elle modifie la liste originale et ne retourne rien)
    m.sort()  # Les éléments de 'm' sont maintenant ordonnés du plus petit au plus grand

    # On veut calculer la différence entre le plus grand et le plus petit nombre de la liste 'm'
    # Puisque 'm' est ordonnée, m[0] est le plus petit élément (première position, car l'indexation commence à 0)
    # m[-1] est une notation spéciale en Python qui accède au dernier élément d'une liste (ici, le plus grand car la liste est triée)
    ans = m[-1] - m[0]  # On stocke la différence entre le plus grand et le plus petit nombre trouvé

    # On affiche le résultat obtenu précédemment à l'écran
    # print() envoie la valeur de 'ans' convertie en chaîne sur la sortie standard (l'écran, sauf redirection)
    print(ans)

# Cette condition spéciale en Python permet de s'assurer que le code du bloc 'main()' ne sera exécuté
# que si ce fichier est lancé directement comme programme principal, pas s'il est importé comme un module
if __name__ == "__main__":  # Si cette condition est vraie (le script est le programme principal exécuté)
    main()  # Alors on appelle la fonction principale pour démarrer le programme