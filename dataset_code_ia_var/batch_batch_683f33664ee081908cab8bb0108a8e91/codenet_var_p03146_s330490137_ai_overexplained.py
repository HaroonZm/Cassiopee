# Définition de la fonction calc qui prend un argument n (supposé être un entier)
def calc(n):
    # La condition suivante vérifie si n est un nombre pair
    # L'opérateur % est le modulo, il renvoie le reste de la division de n par 2
    if n % 2 == 0:
        # Si n est pair (le reste est 0), alors on retourne la moitié de n
        # La division n/2 donne un flottant, donc on convertit le résultat en entier avec int()
        return int(n / 2)
    else:
        # Si n n'est pas pair (donc il est impair), on effectue l'opération 3*n+1
        # On convertit aussi le résultat final en entier, même si ici c'est normalement inutile car 3*n+1 donne un entier
        return int(3 * n + 1)

# Demande à l'utilisateur de saisir une valeur
# input() retourne un texte (string), il faut donc le convertir en entier avec int()
s = int(input())

# On crée une liste appelée num qui contiendra les nombres générés
# On initialise cette liste avec la valeur saisie par l'utilisateur en premier élément
num = [s]

# On définit une variable count qui servira à savoir à quelle étape du calcul on est
# On commence à zéro, ce qui correspond à la position du premier élément dans la liste num
count = 0

# On entre dans une boucle infinie, while True, qui va fonctionner jusqu'à ce qu'on décide d'en sortir avec un break
while True:
    
    # On utilise la fonction calc pour calculer le prochain nombre à partir du nombre courant
    # num[count] donne le dernier nombre ajouté à la liste
    ans = calc(num[count])
    
    # On vérifie ensuite si le nouveau nombre (ans) est déjà présent dans la liste num
    # Cela permet de détecter des répétitions ou des cycles dans la séquence produite
    if ans in num:
        # Si ans est déjà dans num, cela veut dire que la séquence est entrée dans une boucle
        # On affiche le nombre d'étapes effectuées plus 2
        # count commence à 0, donc la première valeur entrée par l'utilisateur correspond à count == 0
        # On ajoute 2 car il y a la première valeur (étape 1) et le nombre répété (étape en cours + 1)
        print(count + 2)
        # On sort de la boucle infinie avec l'instruction break pour arrêter le script
        break
    # Si ans n'est pas encore dans la liste num, on l'y ajoute à la fin avec append
    num.append(ans)
    # On incrémente count de 1 pour avancer à l'étape suivante lors de la prochaine boucle
    count += 1