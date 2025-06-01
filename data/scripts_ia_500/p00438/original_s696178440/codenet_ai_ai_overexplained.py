import sys  # Importe le module sys qui permet d'interagir avec les entrées/sorties du système, notamment pour lire des lignes depuis l'entrée standard.
import copy # Importe le module copy. Ici, il n'est pas utilisé dans le code, mais ce module sert généralement à copier des objets en Python.

# Définition de la fonction principale appelée quand on exécute ce script.
def main():
    # Lecture d'une ligne depuis l'entrée standard, ce sera la première ligne du cas test.
    line = sys.stdin.readline()
    # Tant que la ligne lue, une fois découpée en mots séparés par espace, n'est pas égale à ["0", "0"]
    # Cela signifie que la boucle continuera tant que l'utilisateur ne rentrera pas la chaîne "0 0" qui signifie fin.
    while line.split() != ["0","0"]:
        # Appel de la fonction analy qui traitera la ligne lue et tout ce qui suit pour un cas de données.
        analy(line)
        # Lecture de la ligne suivante pour le prochain cas éventuel ou pour finir la boucle.
        line = sys.stdin.readline()
    # Fin de fonction main, rien à retourner.
    return

# Fonction analy qui prend une chaîne de caractères en argument représentant une ligne.
def analy(line):
    # La ligne est découpée en sous-chaînes selon les espaces et chaque élément converti en entier pour constituer une liste 'field'
    # Par exemple : '3 2' devient [3, 2]
    field = [int(n) for n in line.split()]
    
    # Lecture du nombre d'enregistrements/data qui seront lus dans la suite.
    num = int(sys.stdin.readline())
    # Initialisation d'une liste vide qui contiendra des sous-listes de données entières.
    data = []
    # Pour chaque enregistrement parmi les 'num' à lire
    for i in range(num):
        a = sys.stdin.readline()  # Lit une ligne du flux d'entrée.
        b = [int(n) for n in a.split()]  # Convertit cette ligne (ex: "1 2") en liste d'entiers (ex: [1, 2])
        data.append(b)  # Ajoute cette liste dans 'data', création d’une liste de coordonnées ou points.
    # Affiche le résultat retourné par la fonction compute qui fait le calcul principal,
    # en lui passant la configuration 'field' et la liste des points bloqués 'data'.
    print (compute(field, data))

# Fonction compute prenant en arguments 'field' une liste de 2 entiers et 'ng' une liste de listes d'entiers.
def compute(field, ng):
    # Initialisation d'une liste vide qui servira à stocker des valeurs de chemin ou comptages.
    list = []
    # Double boucle imbriquée : parcours de toutes les lignes du terrain (de 0 à field[1]-1)
    for i in range(field[1]):
        # Parcours de toutes les colonnes du terrain (de 0 à field[0]-1)
        for j in range(field[0]):
            # Si on est sur la première ligne (i == 0)
            if i == 0 :
                # Si la position (j+1, i+1) est dans la liste 'ng' (coordonnées bloquées)
                # Remarque : les coordonnées dans 'ng' semblent 1-indexées alors que i,j sont 0-indexés.
                if [j+1,i+1] in ng:
                    list.append(0)  # On ajoute 0 car chemin bloqué à cet endroit.
                elif j == 0:
                    # Si on est en début de ligne donc tout à gauche et pas bloqué,
                    # alors on peut poser 1 chemin possible (point de départ)
                    list.append(1)
                else:
                    # Sinon on copie la valeur précédente (en colonnes) qui correspond aux chemins possibles.
                    list.append(list[j-1])
            else:
                # Si on est pas sur la première ligne
                if [j+1,i+1] in ng:
                    # Si la case est bloquée, on met la valeur à 0 (pas de chemin possible ici)
                    list[j] = 0
                elif j != 0:
                    # Sinon on ajoute à list[j] la valeur à gauche (list[j-1]) plus la valeur au-dessus (list[j])
                    # Ce calcul correspond à la somme des chemins possibles venant de gauche et du dessus.
                    list[j] = list[j-1] + list[j]
                # Note : si j == 0 pour i > 0, aucun traitement n'est fait dans ce code,
                # ce qui laisse la valeur list[0] inchangée pour les lignes suivantes.
    # Retourne la dernière valeur de la liste qui contient le nombre total de chemins possibles jusqu'en bas à droite.
    return list[len(list)-1]

# Condition spéciale indiquant que ce code est exécuté seulement si ce fichier est lancé directement,
# et pas lorsque ce module est importé ailleurs.
if __name__ == "__main__":
    main()  # Appelle la fonction principale main() qui démarre le programme.