# Initialisation de la variable qui servira à compter un certain total
cnt = 0  # On initialise 'cnt' à 0. Cette variable va accumuler une somme lors du parcours.

# Lecture de plusieurs entiers sur une seule ligne
a, b, n = map(int, input().split())
# 'input()' permet de lire une ligne de texte envoyée depuis l'extérieur du programme (généralement via le clavier).
# La méthode 'split()' découpe la ligne de texte à chaque espace, produisant une liste de chaînes de caractères.
# 'map(int, ...)' applique la conversion d'entiers à chaque élément de la liste obtenue.
# Enfin, la notation 'a, b, n = ...' affecte respectivement les trois premiers entiers à 'a', 'b' et 'n'.

# Lecture des valeurs initiales de largeur et hauteur
w, h = map(int, input().split())
# Même principe que précédemment : on lit deux entiers qui correspondent à une largeur 'w' et une hauteur 'h'.

# Boucle pour traiter les éléments suivants
for i in range(1, n):
    # 'range(1, n)' crée une séquence de nombres commençant à 1 (inclus) jusqu'à n (exclu),
    # ce qui permet d'itérer exactement n-1 fois (puisque souvent un élément initial a déjà été traité hors boucle).
    mw, mh = map(int, input().split())
    # Lecture de deux entiers pour chaque itération : une nouvelle largeur 'mw' et une nouvelle hauteur 'mh'.

    # Condition pour décider comment mettre à jour 'cnt'
    if (h < mh and w > mw) or (h > mh and w < mw):
        # Ce bloc s'exécute si la hauteur augmente et la largeur diminue (ou vice versa, la hauteur diminue et la largeur augmente)
        # Cela signifie qu'il y a une progression "croisée" entre les dimensions.
        # On ajoute à 'cnt' la somme des différences absolues entre anciennes et nouvelles dimensions.
        cnt += abs(mh - h) + abs(mw - w)
        # 'abs()' donne la valeur absolue (toujours positive).
        # La différence de largeur (w à mw) et de hauteur (h à mh) sont additionnées puis ajoutées à 'cnt'.
    else:
        # Ce bloc se produit si la progression n'est pas "croisée",
        # c’est-à-dire si les deux dimensions augmentent, diminuent, ou restent inchangées dans le même sens.
        # Dans ce cas, on ajoute la plus grande différence parmi la hauteur ou la largeur à 'cnt'.
        cnt += max(abs(h - mh), abs(w - mw))
        # 'max()' retourne la valeur la plus élevée des deux arguments.

    # Mise à jour de la largeur et de la hauteur pour la prochaine itération
    w = mw  # On donne à 'w' la valeur de la nouvelle largeur lue
    h = mh  # On donne à 'h' la valeur de la nouvelle hauteur lue
    # Cela garantit que lors de l'itération suivante, on comparera les nouvelles valeurs aux bonnes références.

# Affichage du résultat final
print(cnt)
# Affiche la valeur totale de 'cnt', c'est-à-dire la somme accumulée selon les règles précédemment décrites.