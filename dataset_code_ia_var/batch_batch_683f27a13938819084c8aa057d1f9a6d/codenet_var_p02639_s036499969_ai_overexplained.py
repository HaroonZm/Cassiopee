import sys  # Importe le module sys qui fournit des fonctions et variables utilisées pour manipuler différentes parties de l'exécution Python (comme stdin, l'entrée standard).

# Modifie la limite de récursion maximale que Python autorise.
# Par défaut, Python limite la profondeur de récursion pour éviter le dépassement de pile.
# Ici, on la fixe à 2147483647, ce qui est extrêmement élevé (2^31-1),
# probablement pour éviter les erreurs de récursion dans des situations extrêmes.
sys.setrecursionlimit(2147483647)

# Remplace la fonction d'entrée standard 'input' par 'sys.stdin.readline'.
# Cela permet de lire une ligne de l'entrée standard beaucoup plus rapidement,
# car 'sys.stdin.readline()' est généralement plus performant que 'input()' pour la lecture de grandes quantités de données.
input = sys.stdin.readline

def main():
    # La fonction principale du programme.
    
    # Utilise la fonction 'input()', qui a été redéfinie précédemment pour utiliser 'sys.stdin.readline'.
    # Lit une ligne de texte depuis l'entrée standard (généralement le clavier ou un flux de données).
    # La ligne lue contient normalement des entiers séparés par des espaces qui doivent être traités.
    # La méthode 'split(' ')' va diviser cette ligne en une liste de chaînes de caractères, où chaque chaîne correspond à un nombre.
    # Par exemple, si l'entrée est "1 0 1", 'split(' ')' va produire ['1', '0', '1'].
    # Ensuite, 'map(int, ...)' transforme chaque élément de la liste (qui est une chaîne) en un entier.
    # Enfin, 'list(...)' convertit l'objet map en une véritable liste Python d'entiers.
    x = list(map(int, input().split(' ')))
    
    # Calcule la somme de tous les éléments de la liste 'x' en utilisant la fonction native 'sum()'.
    # Par exemple, si x = [1, 0, 1], alors sum(x) = 2.
    # Ensuite, on soustrait cette somme au nombre 15.
    # Le but est généralement de savoir combien il manque pour atteindre 15.
    # Le résultat de cette opération est ensuite imprimé sur la sortie standard (généralement l'écran).
    print(15 - sum(x))

# Ce bloc conditionnel spécial vérifie si ce script est exécuté comme programme principal (et non importé comme module).
# La variable magique '__name__' vaut '__main__' seulement si le script est lancé directement.
# Si c'est le cas, on appelle la fonction 'main()' pour démarrer l'exécution du programme.
if __name__ == '__main__':
    main()