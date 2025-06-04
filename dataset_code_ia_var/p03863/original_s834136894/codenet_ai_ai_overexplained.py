import collections  # Importe le module collections qui contient des structures de données avancées comme Counter

def main():
    # Lit l'entrée utilisateur, la convertit en chaîne de caractères (str), puis en liste de caractères
    # Cela permet de manipuler chaque caractère individuellement
    s = list(str(input()))

    # Utilise la classe Counter du module collections pour compter combien de fois chaque caractère apparaît dans la liste
    # Counter retourne un dictionnaire où les clés sont les éléments (ici les caractères) et les valeurs sont leur nombre d'occurrences
    l = collections.Counter(s)

    # Vérifie si le nombre de types de caractères différents dans la liste est exactement égal à 2
    # len(l) donne le nombre de clés uniques dans le Counter, donc le nombre de caractères différents
    if len(l) == 2:
        print("Second")  # Si c'est exactement 2, affiche "Second"
    else:
        # Sinon, vérifie si le premier caractère de la liste s (s[0]) est identique au dernier caractère (s[-1])
        if s[0] == s[-1]:
            # Si c'est vrai, teste si la longueur de la liste s est paire
            # len(s) donne le nombre total de caractères; len(s)%2 calcule le reste de la division par 2
            # Si le reste est 0, cela veut dire que la longueur est paire
            if len(s)%2 == 0:
                print("First")  # Si la longueur est paire, affiche "First"
            else:
                print("Second")  # Si la longueur est impaire, affiche "Second"
        else:
            # Si le premier et le dernier caractère ne sont pas identiques
            # Vérifie à nouveau si la longueur de la liste s est paire
            if len(s)%2 == 0:
                print("Second")  # Si paire, affiche "Second"
            else:
                print("First")   # Si impaire, affiche "First"

# Ce bloc conditionnel vérifie si le script est exécuté directement (et pas importé)
# Si __name__ est égal à "__main__", le code à l'intérieur est exécuté
# Cela permet de définir un point d'entrée principal pour le script
if __name__ == "__main__":
    main()  # Appelle la fonction main pour commencer l'exécution du programme