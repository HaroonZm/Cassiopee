def read_input():
    """
    Lit les entrées de l'utilisateur ligne par ligne jusqu'à ce qu'une erreur d'entrée survienne (EOF ou interruption).
    Chaque ligne est supposée contenir un mot et un nombre séparés par un espace.
    Retourne un dictionnaire où chaque clé est un mot et la valeur est une liste de chaînes représentant les nombres associés à ce mot.
    """
    result = {}
    while True:
        try:
            # Lecture d'une ligne de l'entrée standard
            n = input()
        except Exception:
            # Fin de l'entrée (EOF ou interruption)
            break
        # Séparation de la ligne en mot et nombre
        word, number = n.split()
        # Ajoute le nombre à la liste associée au mot dans le dictionnaire
        if word in result:
            result[word].append(number)
        else:
            result[word] = [number]
    return result

def afficher_resultats(result):
    """
    Prend en entrée un dictionnaire associant des mots à des listes de chaînes de chiffres.
    Pour chaque mot (clé), affiche le mot suivi d'une ligne contenant la liste triée de ses valeurs numériques (converties en entiers puis en chaînes, triées par ordre croissant).
    L'affichage se fait dans l'ordre alphabétique des mots.
    """
    # Parcours des éléments du dictionnaire, triés par clé
    for k, v in sorted(result.items()):
        # Conversion des valeurs en entier, tri, puis re-conversion en chaînes
        val = sorted(list(map(int, v)))
        # Affichage du mot et de ses valeurs triées
        print(k + '\n' + ' '.join(map(str, val)))

def main():
    """
    Point d'entrée principal du programme.
    Lit les entrées utilisateur, organise les données, puis affiche les résultats triés.
    """
    # Lecture et organisation des entrées dans un dictionnaire
    result = read_input()
    # Affichage des résultats selon les critères spécifiés
    afficher_resultats(result)

# Exécution du programme
if __name__ == "__main__":
    main()