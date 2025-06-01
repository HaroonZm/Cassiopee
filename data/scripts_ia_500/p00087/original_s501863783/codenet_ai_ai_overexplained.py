import sys  # Importe le module 'sys' qui permet d'interagir avec des parties du système, ici utilisé pour la lecture d'entrée standard

st = []  # Initialise une liste vide appelée 'st' qui va servir de pile pour stocker des nombres et résultats intermédiaires

for a in sys.stdin:  # Pour chaque ligne lue depuis l'entrée standard (par exemple l'utilisateur ou un fichier redirigé)
    s = a.split()  # Divise la ligne en une liste de chaînes de caractères, séparées par défaut par des espaces
    del st[:]  # Vide la liste 'st' en supprimant tous ses éléments, préparer pour une nouvelle expression
 
    for i in range(len(s)):  # Itère sur chaque index dans la liste 's', pour traiter chaque élément un par un
        if s[i] in ['+', '-', '*', '/']:  # Vérifie si l'élément courant est un opérateur mathématique: addition, soustraction, multiplication ou division
            a = st.pop(-1)  # Retire et récupère le dernier élément de la pile 'st', ce sera l'opérande droit ou second opérande (puisque pile LIFO)
            b = st.pop(-1)  # Retire et récupère nouvellement le dernier élément restant dans la pile, qui est l'opérande gauche ou premier opérande
            # Effectue l'opération correspondante selon l'opérateur trouvé
            if s[i] == '+':  
                c = b + a  # Additionne b et a
            elif s[i] == '-':
                c = b - a  # Soustrait a de b
            elif s[i] == '*':
                c = b * a  # Multiplie b par a
            else:
                c = 1. * b / a  # Divise b par a et multiplie par 1. pour forcer un résultat flottant (évite la division entière)
            st.append(c)  # Ajoute le résultat de l'opération 'c' au sommet de la pile pour pouvoir être utilisé par la suite
        else:
            # L'élément n'est pas un opérateur, donc c'est un nombre sous forme texte que l'on convertit en float
            st.append(float(s[i]))  # Convertit en nombre flottant et ajoute ce nombre dans la pile 'st'
    print st[0]  # Après avoir parcouru toute la ligne, le résultat final est le seul élément dans la pile; on l'affiche ici