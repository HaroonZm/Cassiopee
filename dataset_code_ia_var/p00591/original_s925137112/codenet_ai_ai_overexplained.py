import sys  # Importe le module sys qui permet d'accéder à certaines fonctionnalités du système d'exploitation, dont l'accès à l'entrée standard stdin pour lire des données

# Boucle infinie, elle continuera à s'exécuter jusqu'à la rencontre d'une instruction break qui l'arrête. C'est utile quand on ne sait pas à l'avance combien d'itérations il y aura.
while True:
    # Lecture d'une ligne depuis l'entrée standard via sys.stdin.readline(). 
    # .rstrip() supprime les éventuels retours à la ligne et espaces inutiles à droite de la ligne lue.
    # int(...) convertit la chaîne de caractères obtenue en un entier.
    n = int(sys.stdin.readline().rstrip())
    # Si n vaut 0, cela signifie qu'il faut arrêter le programme selon la logique (souvent utilisé comme cas d'arrêt dans les entrées de type compétitions).
    if n == 0:
        # break interrompt immédiatement la boucle la plus proche, ici le while True.
        break
    # Création d'une liste vide qui va contenir les informations sur les étudiants, chaque élève étant représenté par une liste d'entiers.
    students = []
    # Boucle for qui s'exécute n fois (pour chaque étudiant à traiter)
    for i in range(n):
        # Lecture de la ligne suivant l'entier n sur l'entrée standard.
        # .rstrip() supprime à nouveau les espaces et \n de fin inutile.
        # .split(' ') divise la chaîne en morceaux à chaque espace, ce qui génère une liste de chaînes représentant les éléments d'une ligne.
        # map(int, ...) convertit chaque morceau de la liste en entier.
        # list(...) convertit l'objet map obtenu en liste de valeurs entières.
        students.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
    # s_list sera une nouvelle liste de listes décrivant, pour chaque case d'un étudiant (lignes), si la valeur correspond au minimum de la ligne.
    # Syntaxe utilisée : compréhension de liste imbriquée qui fonctionne ainsi:
    #     Pour chaque 'row' dans students, on construit une liste de booléens.
    #     Pour chaque 's' dans la 'row', on vérifie si min(row)==s (si c'est le minimum de la ligne).
    s_list = [[min(row) == s for s in row] for row in students]
    # t_list sera une liste de listes correspondant aux "colonnes" du tableau (soit par matière, soit par question, etc. par étudiant).
    # zip(*students) fait une "transposée" du tableau, c’est-à-dire que les lignes deviennent des colonnes.
    # Pour chaque 'col' dans la transposée, on génère une liste de booléens : pour chaque 's' de la colonne, on teste si c'est le maximum de la colonne.
    t_list = [[max(col) == s for s in col] for col in zip(*students)]
    # Initialisation de la liste 'ret' contenant une première valeur 0. Elle contiendra tous les éléments qui satisfont une condition donnée ci-dessous.
    ret = [0]
    # Boucle sur les indices et données; enumerate retourne à la fois l'index (i) et l'objet (data) lors de l'itération sur le zip de s_list et de la transposée de t_list.
    for i, data in enumerate(zip(s_list, zip(*t_list))):
        # data est composé du couple (ligne de s_list, colonne de t_list pour cette ligne)
        # On zippe les deux pour comparer chaque colonne d'une même ligne.
        for j, d in enumerate(zip(*data)):
            # d est un tuple de deux booléens, un indiquant si l'élément de la ligne est le minimum, l'autre si c'est le maximum de la colonne.
            # all(d) vérifie que tous les éléments de d sont True, soit que l'élément est à la fois minimum de sa ligne ET maximum de sa colonne.
            if all(d):
                # On ajoute la valeur correspondante (soit students[i][j]) à la liste des résultats potentiels.
                ret.append(students[i][j])
    # Affichage du résultat final, qui est le maximum de la liste ret (qui contient au moins 0, et éventuellement d'autres éléments trouvés ci-dessus).
    print(max(ret))