def main():
    # Ceci est la fonction principale 'main' qui va contenir tout le processus du programme.

    # Définir une liste vide qui contiendra des entiers. 
    # Les listes sont des structures de données qui peuvent stocker plusieurs éléments.
    DAT = []

    # Lire un entier tapé par l'utilisateur. La fonction input() lit l'entrée en tant que chaîne de caractères.
    # La fonction int() convertit cette chaîne en entier.
    num = int(input())

    # Boucler 'num' fois. range(num) crée une séquence de 0 à num-1.
    for i in range(num):
        # Pour chaque itération, lire une ligne à partir de l'utilisateur.
        # La méthode input() lit la ligne comme une chaîne.
        # La méthode split() divise la ligne en une liste de sous-chaînes basées sur les espaces.
        # map(int, ...) convertit chaque sous-chaîne en entier.
        # list(...) convertit le résultat de map en une liste de deux entiers.
        x, y = list(map(int, input().split()))
        # Ajouter le premier entier x à la liste DAT à la fin, grâce à append().
        DAT.append(x)
        # On répète ceci pour chaque itération : seul x est ajouté à ce stade. y n'est pas encore ajouté.

    # Ajouter y à la liste DAT après avoir terminé la boucle. 
    # A ce moment, y vaut la dernière valeur obtenue dans la boucle précédente.
    # Cela garantit que DAT contient 'num+1' valeurs.
    DAT.append(y)

    # Calculer le nombre total d'éléments : c'est num+1 car on a ajouté un élément supplémentaire.
    num1 = num + 1

    # Créer une matrice 2D appelée TBL, contenant des zéros.
    # Cette matrice a num1 lignes et num1 colonnes (c'est-à-dire num+1 lignes et colonnes).
    # L'expression [0] * num1 crée une ligne de zéros de longueur num1.
    # La compréhension de liste répète cela num1 fois, donc on obtient une liste de listes (une matrice).
    TBL = [[0] * num1 for i in range(num1)]

    # Première boucle : 'i' va de 0 à num1-1 (inclus). Cette boucle va déterminer la "distance" entre les indices de la matrice.
    for i in range(0, num1):
        # Deuxième boucle : 'row' va de 0 à num-i-1, c'est-à-dire tous les départs possibles pour une sous-séquence de cette distance.
        for row in range(num - i):
            # Calculer 'col' comme le dernier indice de la sous-séquence parcourue.
            # col est fixé à row + i + 1, donc le segment considéré va de row à col inclusivement.
            col = row + i + 1
            # Troisième boucle : 'j' va de row+1 à col-1 (exclu col), parcourant tous les points de séparation intermédiaires.
            for j in range(row + 1, col):
                # On va calculer une nouvelle valeur 'x' basée sur l'éclatement à la position j dans le segment [row, col].
                # DAT[row], DAT[j], et DAT[col] sont multipliés, puis on ajoute TBL[row][j] et TBL[j][col].
                # Cela ressemble à une étape de programmation dynamique pour optimiser un coût de multiplication séquentielle.
                x = DAT[row] * DAT[j] * DAT[col] + TBL[row][j] + TBL[j][col]
                # Test pour savoir si c'est la première fois que l'on remplit TBL[row][col] (valeur initiale 0),
                # ou si la valeur calculée 'x' est meilleure (ici on cherche le maximum, car on remplace si x > TBL[row][col]).
                if TBL[row][col] < 1 or TBL[row][col] > x:
                    TBL[row][col] = x

    # Après tous les calculs, afficher le contenu final de TBL[row][col],
    # où 'row' et 'col' sont les dernières valeurs utilisées dans la boucle précédente.
    # Cette ligne affiche le résultat sous forme de chaîne grâce à "{}".format(...)
    print("{}".format(TBL[row][col]))

# Ceci est le point d'entrée du script. Lorsque le fichier est exécuté directement,
# la condition ci-dessous s'évalue à True, et la fonction main() est appelée.
# Si le fichier est importé comme module, ce bloc ne s'exécutera pas.
if __name__ == '__main__':
    main()