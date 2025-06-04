# Prend quatre entiers donnés en entrée, séparés par des espaces
# La fonction input() lit une ligne de texte tapée par l'utilisateur au clavier
# La fonction split() coupe cette ligne en morceaux (appelés "tokens") selon les espaces
# La fonction map(int, ...) transforme chaque token en entier (int)
# Les quatre entiers lus sont assignés respectivement aux variables h, w, s, t
h, w, s, t = map(int, input().split())

# On vérifie ici si le produit de h et w (c'est-à-dire h fois w) est impair
# L'opérateur * fait la multiplication
# Le symbole % calcule le reste de la division euclidienne (modulo)
# Si h*w%2==1 cela veut dire que le produit est impair (reste 1 quand on divise par 2)
if h * w % 2 == 1:
    # Bloc exécuté seulement si la condition précédente est vraie (i.e., produit impair)
    
    # On additionne s et t, puis on prend le reste de la division par 2
    # Si (s+t)%2==1 alors la somme s+t est impaire
    if (s + t) % 2 == 1:
        # Si la somme est impaire, on affiche "No"
        # La fonction print() affiche un message à l'écran
        print("No")
    else:
        # Sinon (donc si la somme est paire), on affiche "Yes"
        print("Yes")
else:
    # Bloc alternatif qui s'exécute si le produit h*w est pair (donne un reste de 0 quand on divise par 2)
    # Dans ce cas on affiche directement "Yes", peu importe les valeurs de s et t
    print("Yes")