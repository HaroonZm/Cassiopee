def counting_sort(a, b, k):
    # Crée une liste c de taille k, initialisée à 0.
    # Cette liste sera utilisée pour compter le nombre de fois que chaque valeur apparaît dans 'a'.
    # 'k' doit être supérieur au plus grand élément dans 'a', car les indices vont de 0 à k-1.
    c = [0 for _ in range(k)]  # [0 for _ in range(k)] crée une liste remplie de zéros, de taille k.
    
    # Parcours chaque élément de la liste 'a' pour compter les occurrences.
    for i in range(len(a)):
        # a[i] est la valeur à la position i.
        # Incrémente la valeur à l'indice correspondant dans 'c'.
        # Cela compte combien de fois chaque valeur apparaît dans 'a'.
        c[a[i]] += 1  # Ajoute 1 à c[a[i]], c'est-à-dire compte le nombre d'occurrences de 'a[i]' dans 'a'.
    
    # Modifie la liste 'c' pour qu'elle contienne les positions cumulées.
    for i in range(1, k):
        # Ajoute à c[i] la somme de tous les comptes précédents.
        # Cela permet de savoir jusqu'à quel indice une valeur doit être placée dans le tableau résultat.
        c[i] += c[i-1]  # c[i] devient la somme des comptes jusque i inclus.
    
    # Parcours les éléments de 'a' dans l'ordre original.
    for i in range(len(a))[::1]:  # [::1] permet de parcourir la liste de gauche à droite, équivalent à range(len(a))
        # Place a[i] à la bonne position dans la sortie 'b'
        # c[a[i]] - 1 donne la position correcte, car les indices démarrent à 0.
        b[c[a[i]] - 1] = a[i]  # Place a[i] à cette position dans 'b'
        # Décrémente le compteur, pour le prochain élément identique (en cas de doublon).
        c[a[i]] -= 1  # Réduit de 1 la position disponible pour cette valeur.
    
    # Renvoie la liste triée 'b'.
    return b

def main():
    # Lit un nombre entier, qui représente le nombre d'éléments à trier.
    n = int(input())  # La fonction input() lit une ligne, int() convertit la chaîne en entier.
    # Lis une ligne d'entrée, la découpe avec split() (sur les espaces), puis convertit chaque morceau en entier.
    # map(int, ...) applique int() à chaque sous-chaîne.
    A = list(map(int, input().split()))  # Construit la liste A des entiers à trier.
    
    # Initialise une nouvelle liste B de même taille que A, remplie de zéros.
    B = [0 for _ in range(len(A))]  # Prépare la liste qui contiendra le résultat trié.
    
    # Appelle counting_sort pour trier la liste A.
    # 'max(A) + 1' donne la taille k de la liste des compteurs, car les valeurs dans A vont de 0 à max(A).
    b = counting_sort(A, B, max(A) + 1)
    
    # Affiche la liste triée en joignant les entiers avec des espaces.
    # map(str, b) convertit chaque élément de 'b' en chaîne de caractères.
    # " ".join(...) combine ces chaînes avec des espaces intermédiaires.
    print(" ".join(map(str, b)))

# Point d'entrée du programme.
# Vérifie que ce fichier est exécuté directement (et non importé comme module).
if __name__ == "__main__":
    main()  # Lance la fonction principale.