def classify_tensions():
    """
    Lit en boucle des paires de valeurs flottantes représentant deux tensions,
    puis les classifie selon des critères prédéfinis en affichant la catégorie correspondante.

    Le programme attend que l'utilisateur entre deux nombres flottants séparés par un espace.
    Si l'entrée est invalide ou qu'une erreur de conversion se produit, la boucle s'arrête.

    Pour chaque paire de tensions (t1, t2) lues :
    - Les tensions sont multipliées par 100 et converties en entiers pour comparaison.
    - En fonction des seuils prédéfinis pour t1 et t2, une catégorie est affichée :
        "AAA", "AA", "A", "B", "C", "D", "E" ou "NA" si aucune catégorie ne correspond.

    Exemple d'utilisation:
    > 34.5 68.0
    AAA
    > 40.0 83.0
    A
    > (entrée invalide ou EOF)
    (fin du programme)
    """
    while True:
        try:
            # Lecture d'une ligne d'entrée et séparation en deux valeurs
            t1, t2 = map(float, input().split())
        except:
            # Fin de saisie ou erreur, sortie de la boucle
            break

        # Conversion des tensions en centièmes pour simplifier les comparaisons
        t1, t2 = int(t1 * 100), int(t2 * 100)

        # Test des intervalles pour déterminer la catégorie
        if t1 < 3550 and t2 < 7100:
            print("AAA")
        elif t1 < 3750 and t2 < 7700:
            print("AA")
        elif t1 < 4000 and t2 < 8300:
            print("A")
        elif t1 < 4300 and t2 < 8900:
            print("B")
        elif t1 < 5000 and t2 < 10500:
            print("C")
        elif t1 < 5500 and t2 < 11600:
            print("D")
        elif t1 < 7000 and t2 < 14800:
            print("E")
        else:
            # Si aucune condition n'est satisfaite, on affiche "NA"
            print("NA")


# Appel de la fonction principale pour lancer la classification        
if __name__ == "__main__":
    classify_tensions()