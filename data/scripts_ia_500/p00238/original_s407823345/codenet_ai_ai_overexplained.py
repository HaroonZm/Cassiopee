import sys  # Importation du module sys qui permet d'accéder à des variables et fonctions liées au système d'exploitation et à l'environnement d'exécution Python.

# Définition d'une fonction nommée 'solve' qui prend un argument 't'
def solve(t):
    # Convertit la valeur d'entrée (str) en entier et le stocke dans la variable 'n'
    n = int(input())
    # Boucle for qui s'exécute 'n' fois. Le caractère '_' est utilisé comme variable temporaire non utilisée
    for _ in range(n):
        # Lit une ligne de texte de l'entrée standard, la divise en deux parties séparées par un espace,
        # convertit ces deux parties en entiers, et les attribue respectivement aux variables 's' et 'f'
        s, f = map(int, input().split())
        # Calcule la différence entre 'f' et 's' (durée d'une tâche) et la soustrait de la variable 't'
        t -= (f - s)
    # Après avoir soustrait toutes les durées, retourne la chaîne 'OK' si 't' est inférieur ou égal à 0,
    # sinon retourne la valeur restante de 't', ce qui indique le temps restant d'étude
    return 'OK' if t <= 0 else t

# Définition de la fonction principale 'main' qui prend une liste d'arguments (non utilisée ici)
def main(args):
    # Boucle infinie qui continue à tourner jusqu'à ce qu'une condition d'arrêt soit rencontrée
    while True:
        # Lit une ligne de l'entrée standard, la convertit en entier et la stocke dans la variable 't'.
        # Cette variable représente le temps total initial disponible pour étudier.
        t = int(input())
        # Condition pour sortir de la boucle principale lorsque 't' vaut 0,
        # indiquant qu'il n'y a plus de cas à traiter
        if t == 0:
            # Utilisation de 'break' pour interrompre la boucle infinie
            break
        # Appelle la fonction 'solve' avec le temps initial 't' et récupère le résultat dans 'ans'
        ans = solve(t)
        # Affiche le résultat obtenu, soit 'OK' en cas d'épuisement du temps, soit le temps restant
        print(ans)

# Condition qui vérifie si ce script est exécuté directement et non importé en tant que module dans un autre script
if __name__ == '__main__':
    # Appelle la fonction principale 'main' avec la liste des arguments de la ligne de commande à partir du deuxième élément
    # (le premier élément sys.argv[0] est le nom du script lui-même)
    main(sys.argv[1:])