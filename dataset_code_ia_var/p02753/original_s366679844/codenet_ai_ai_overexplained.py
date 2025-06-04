# Définition de la fonction principale qui sera le point d'entrée du programme
def main():
    # Utilisation de la fonction input() pour demander à l'utilisateur de saisir une chaîne de caractères.
    # La chaîne obtenue est ensuite convertie en une liste de caractères avec la fonction list().
    # Par exemple, si l'utilisateur tape 'ABA', stop vaudra ['A', 'B', 'A'].
    stop = list(input())

    # Initialisation de deux variables entières, a et b, en les mettant à zéro.
    # Ces variables serviront à compter respectivement le nombre de caractères 'A' et le nombre de caractères qui ne sont pas 'A'.
    a, b = 0, 0

    # Début d'une boucle for qui va parcourir chaque élément (chaque caractère) de la liste 'stop'.
    for i in stop:
        # Condition if qui vérifie si le caractère courant 'i' est égal à la chaîne de caractère 'A'.
        # L'opérateur == sert à vérifier l'égalité entre deux valeurs.
        if 'A' == i:
            # Si la condition est vraie, c'est-à-dire si le caractère est 'A', on augmente la valeur de la variable 'a' de 1.
            a += 1
        else:
            # Si la condition est fausse, c'est-à-dire que le caractère n'est pas 'A', on augmente la valeur de la variable 'b' de 1.
            b += 1

    # Après la boucle, tous les caractères ont été analysés et les compteurs 'a' et 'b' ont été mis à jour en conséquence.

    # Vérification si les deux compteurs sont strictement supérieurs à zéro.
    # Cela revient à vérifier s'il y a au moins un 'A' ET au moins un caractère différent de 'A' dans la saisie.
    if a > 0 and b > 0:
        # Si les deux conditions sont vraies, la fonction print() affiche la chaîne de caractères 'Yes' dans la console.
        print('Yes')
    else:
        # Si au moins un des deux compteurs est à zéro, cela signifie qu'il n'y a que des 'A' ou aucun 'A' dans la saisie :
        # la fonction print() affiche alors la chaîne de caractères 'No' dans la console.
        print('No')

# Appel de la fonction main() pour lancer l'exécution du programme.
main()