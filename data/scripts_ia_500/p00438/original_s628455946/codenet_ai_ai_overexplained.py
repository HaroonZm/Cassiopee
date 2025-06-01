import sys  # Importe le module sys, qui permet d'interagir avec des fonctionnalités spécifiques du système d'exploitation, comme la lecture depuis l'entrée standard (stdin).
import copy  # Importe le module copy, utilisé pour dupliquer des objets en Python. (Ici, il n'est pas utilisé dans le code fourni.)

def main():
    # Lit une ligne depuis l'entrée standard (stdin). readline() lit un texte jusqu'au retour à la ligne (\n).
    line = sys.stdin.readline()
    # Tant que la ligne lue n'est pas égale à "0 0" (séparation en liste), on continue le traitement.
    # line.split() découpe la ligne en une liste de chaînes de caractères, en séparant par espaces.
    while line.split() != ["0","0"]:
        analy(line)  # Appelle la fonction analy avec la ligne lue en entrée.
        line = sys.stdin.readline()  # Lit la ligne suivante pour la prochaine itération.
    return  # Retourne None implicitement, indique la fin de la fonction main.

def analy(line):
    # Transforme la chaîne 'line' en une liste d'entiers. 'line.split()' crée une liste de chaînes qu'on convertit avec int().
    field = [int(n) for n in line.split()]
    # Lit un entier depuis l'entrée standard. C'est le nombre d'éléments qui vont suivre.
    num = int(sys.stdin.readline())
    data = []  # Initialise une liste vide qui contiendra les données suivantes.
    for i in range(num):  # Pour chaque élément attendu (de 0 jusqu'à num-1) :
        a = sys.stdin.readline()  # Lit une nouvelle ligne.
        b = [int(n) for n in a.split()]  # Convertit cette ligne en une liste d'entiers.
        data.append(b)  # Ajoute cette liste à la liste data.
    # Appelle la fonction compute avec les paramètres field et data, puis affiche le résultat avec print.
    print(compute(field, data))

def compute(field, ng):
    # Initialise une liste vide qui servira à stocker des valeurs intermédiaires pour le calcul.
    list = []
    # La variable field contient deux valeurs, probablement la taille d'un champ ou grille.
    # On itère sur la deuxième valeur (hauteur ou nombre de lignes).
    for i in range(field[1]):
        # Puis on itère sur la première valeur (largeur ou nombre de colonnes).
        for j in range(field[0]):
            # Vérifie si on est sur la toute première ligne (i==0).
            if i == 0:
                # Si la position actuelle (j+1, i+1) est dans la liste ng (obstacles ou cellules interdites).
                if [j+1,i+1] in ng:
                    list.append(0)  # Ajoute 0 pour cette position, signifiant aucune possibilité ici.
                # Sinon, si on est aussi sur la première colonne (j==0).
                elif j == 0:
                    list.append(1)  # Ajoute 1, initialisant la première position possible.
                else:
                    # Sinon, copie la valeur juste à gauche (j-1) pour cette position.
                    list.append(list[j-1])
            else:
                # Si on est sur une ligne autre que la première.
                if [j+1,i+1] in ng:
                    list[j] = 0  # Si la position est dans ng, la valeur à l'index j devient 0 (bloquée).
                elif j != 0:
                    # Sinon (si on n'est pas sur la première colonne), on modifie la valeur actuelle.
                    # Additionne la valeur précédente (gauche) plus la valeur actuelle (au-dessus), simulant un calcul combinatoire.
                    list[j] = list[j-1] + list[j]
                # Note: si j == 0 et pas dans ng, la valeur de list[j] ne change pas et reste celle de la ligne précédente.
    # Retourne la dernière valeur de la liste, qui représente le résultat final du calcul.
    return list[len(list)-1]

# Condition qui vérifie que ce script est celui exécuté (et non importé).
if __name__ == "__main__":
    main()  # Lance la fonction principale main.