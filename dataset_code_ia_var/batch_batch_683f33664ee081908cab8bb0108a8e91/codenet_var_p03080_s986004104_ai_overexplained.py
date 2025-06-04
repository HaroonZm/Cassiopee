# Demande à l'utilisateur de saisir un entier et convertit la saisie en entier avec int().
# Ceci détermine la longueur de la chaîne de caractères que nous allons lire ensuite.
N = int(input())

# Demande à l'utilisateur de saisir une chaîne de caractères.
# Cette chaîne aura exactement N caractères selon l'énoncé.
s = input()

# Initialise un compteur à 0. 
# Ce compteur 'num' va compter combien de fois la lettre 'R' apparaît dans la chaîne s.
num = 0

# La boucle for va parcourir chaque index 'i' de 0 jusqu'à N-1 (car range(N) génère les entiers de 0 à N-1).
for i in range(N):
    # Vérifie si le caractère à la position i dans la chaîne s est exactement égal à "R".
    if s[i] == "R":
        # Si oui, on incrémente le compteur 'num' de 1.
        num += 1

# Après avoir parcouru toute la chaîne, on compare le nombre de "R" (num) au nombre de caractères restants, c’est-à-dire N - num.
# Si le nombre de "R" est strictement supérieur au nombre des autres caractères :
if num > N - num:
    # Affiche "Yes" à l'écran, car il y a plus de "R" que d'autres lettres.
    print("Yes")
else:
    # Sinon, si num n'est pas strictement plus grand, affiche "No".
    print("No")