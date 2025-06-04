import sys  # On importe le module sys pour accéder à l'entrée standard sys.stdin

def main(lines=None):
    # ここは変えない
    # Cette section ne doit pas être modifiée conformément à l'instruction du commentaire japonais ci-dessus

    # Vérifie si la variable 'lines' a été passée à la fonction ou non
    # Si lines n'est pas fourni (None ou vide), on lit toutes les lignes données en entrée standard (par ex. dans un terminal)
    if not lines:
        # sys.stdin.readlines() lit toutes les lignes de l'entrée standard et les retourne sous forme de liste de chaînes de caractères
        lines = sys.stdin.readlines()

    # Pour chaque ligne dans la liste 'lines', on découpe la ligne en séparant chaque mot ou nombre (chaîne) sur les espaces
    # Cela transforme "3 4 5\n" en ["3", "4", "5"]
    lines = [line.split() for line in lines]
    # ここまで

    # lines_int va contenir une liste de listes ; chaque sous-liste contient trois entiers triés
    # Pour chaque sous-liste dans 'lines', on convertit chaque chaîne en nombre entier grâce à map(int, line)
    # On transforme l'objet map en liste explicite grâce à list()
    # Ensuite, on utilise sorted(...) pour mettre les éléments dans l'ordre croissant
    lines_int = [sorted(list(map(int, line))) for line in lines]

    # On initialise trois compteurs à zéro. 
    # a : Compte les triangles rectangles trouvés
    # b : Compte les triangles aigus trouvés
    # c : Compte les triangles obtus trouvés
    a = 0
    b = 0
    c = 0

    # On parcourt chaque sous-liste (représente les trois côtés d'un triangle) dans 'lines_int'
    for line in lines_int:
        # Pour que trois longueurs forment un triangle valide, la somme des deux plus petites doit être strictement supérieure à la troisième (la plus grande)
        if line[0] + line[1] > line[2]:
            # Si la somme des carrés des deux petits est exactement égale au carré du grand côté, c'est un triangle rectangle (théorème de Pythagore)
            if line[2] ** 2 == line[0] ** 2 + line[1] ** 2:
                a += 1  # On incrémente le compteur des triangles rectangles
            # Si le carré du plus grand côté est strictement inférieur à la somme des carrés des autres, c'est un triangle aigu (tous les angles < 90°)
            elif line[2] ** 2 < line[0] ** 2 + line[1] ** 2:
                b += 1  # On incrémente le compteur des triangles aigus
            # Si le carré du plus grand côté est strictement supérieur à la somme des carrés des autres, c'est un triangle obtus (un angle > 90°)
            elif line[2] ** 2 > line[0] ** 2 + line[1] ** 2:
                c += 1  # On incrémente le compteur des triangles obtus
        else:
            # Si la somme des deux petits côtés n'est pas supérieure au grand côté, alors on ne peut plus former de triangle avec les lignes suivantes
            # Le programme met fin à la boucle et passe à l'affichage
            # answer = "{0} {1} {2} {3}".format(a + b + c, a, b, c)
            break  # Sortie immédiate de la boucle en cas d'entrée invalide

    # Construction de la chaîne réponse à imprimer
    # a + b + c est le nombre total de triangles valides trouvés
    # Les valeurs de a, b, c sont affichées dans l'ordre demandé
    answer = "{0} {1} {2} {3}".format(a + b + c, a, b, c)

    # Affichage du résultat sur la sortie standard
    print(answer)
    # On retourne la même chaîne pour un éventuel usage dans des tests automatisés
    return answer

def test_main():
    # On définit les entrées de test sous forme d'une seule chaîne multilignes
    test_inputs = """
3 4 5
2 1 2
6 3 4
1 1 1
1 2 3
""".strip()
    # On découpe la chaîne en une liste de lignes (chaque élément est une chaîne de caractères)
    test_inputs = test_inputs.split("\n")
    # On appelle la fonction principale avec ces lignes de test
    answer = main(test_inputs)
    # On définit la sortie attendue sous forme d'une chaîne
    expect = """
4 1 2 1
""".strip()

    # On vérifie que la sortie de la fonction correspond à la sortie attendue
    assert answer == expect

# Ce bloc permet à ce fichier Python d'être exécuté en tant que programme principal
if __name__ == "__main__":
    main()  # On appelle la fonction principale, qui lira depuis l'entrée standard si aucun argument n'est fourni