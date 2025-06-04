import bisect  # On importe le module bisect, qui fournit des fonctions utiles pour manipuler des listes triées.

def main():
    # Lecture de l'entrée utilisateur pour obtenir la valeur n.
    # La fonction input() attend que l'utilisateur saisisse une ligne, puis retourne cette ligne sous forme de chaîne de caractères.
    # La fonction int() convertit cette chaîne de caractères en un nombre entier.
    n = int(input())

    # Lecture d'une liste d'entiers sur une seule ligne.
    # input() lit la ligne saisie par l'utilisateur.
    # split() divise cette ligne en une liste de sous-chaînes (chaque sous-chaîne étant un nombre sous forme textuelle, séparé par des espaces).
    # La compréhension de liste [int(a) for a in input().split()] convertit chaque sous-chaîne en un entier pour obtenir une liste d'entiers que l'on stocke dans 'li'.
    li = [int(a) for a in input().split()]

    # Lecture du nombre de requêtes q à traiter.
    # Convertit la saisie utilisateur en entier comme précédemment.
    q = int(input())

    # On boucle q fois pour traiter chaque requête.
    # L'utilisation de range(q) crée un itérable représentant les indices de 0 à q-1, mais comme nous n'utilisons pas l'indice dans la boucle, on le nomme conventionnellement '_'.
    for _ in range(q):
        # À chaque itération, lecture d'une valeur k à rechercher dans la liste 'li'.
        # On saisit l'entrée, la convertit en entier, et la stocke dans k.
        k = int(input())

        # Utilisation de la fonction bisect_left du module bisect.
        # bisect_left(li, k) recherche la position d'insertion du nombre k dans la liste 'li' déjà triée,
        # de manière à maintenir l'ordre trié. Si k existe déjà dans la liste, bisect_left renverra son premier indice d'apparition,
        # sinon, il donnera la position où k pourrait être inséré pour que la liste reste triée.
        i = bisect.bisect_left(li, k)

        # Affichage de la position trouvée grâce à la fonction print().
        print(i)

# Appel de la fonction main pour démarrer le programme quand le script est exécuté.
main()