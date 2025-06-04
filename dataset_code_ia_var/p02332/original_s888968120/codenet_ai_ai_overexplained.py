def main():
    # Demande à l'utilisateur une entrée, qui doit contenir deux entiers séparés par un espace.
    # Par exemple, si l'utilisateur tape "3 5", alors input() renverra la chaîne "3 5".
    s = input()  # Lecture d'une ligne depuis l'entrée standard (clavier).
    # Utilise la fonction split() pour séparer la chaîne d'entrée là où il y a des espaces,
    # ce qui retourne une liste de chaînes (par exemple, ["3", "5"]).
    lst = s.split()
    # Utilise la fonction map() pour convertir chaque élément de cette liste de chaînes,
    # en entiers. map(int, lst) itère sur chaque élément de lst, applique int(), et retourne un itérable avec les entiers.
    n, k = map(int, lst)  # Attribution multiple : 'n' prendra la première valeur, 'k' la deuxième.

    # Vérifie si la valeur de 'n' est strictement supérieure à la valeur de 'k'.
    # Si c'est le cas, ça veut dire qu'il n'y a pas assez d'éléments pour faire des arrangements, donc la réponse est 0.
    if n > k:
        print(0)  # Affiche le chiffre 0 à l'écran.
        return    # Quitte la fonction main, donc le reste du code n'est pas exécuté.

    # Initialise la variable 'mod' pour stocker la valeur du modulo utilisé dans les calculs.
    # Ici, mod vaut 10^9 + 7, une grande valeur premier couramment utilisée pour éviter les débordements.
    mod = 10 ** 9 + 7

    # Initialise une variable 'ans' pour stocker le résultat final.
    # On la commence à 1 car elle va servir de multiplicateur neutre pour la suite du calcul.
    ans = 1

    # Boucle for qui va itérer 'n' fois, c'est-à-dire pour chaque entier 'i' allant de 0 à n-1.
    for i in range(n):
        # À chaque itération, on multiplie 'ans' par (k - i).
        # Cela permet de calculer le nombre d'arrangements de k objets pris n à n (sans répétition et en tenant compte de l'ordre).
        ans *= k - i

        # Applique le modulo à chaque étape pour éviter que ans ne devienne trop grand
        # et provoque un dépassement de capacité (overflow).
        ans %= mod  # Le résultat maintenant sera toujours compris entre 0 et mod - 1.

    # Affiche la variable 'ans', qui contient maintenant le résultat final du calcul.
    print(ans)

# Ce bloc permet d'exécuter la fonction main() seulement si ce fichier est exécuté comme programme principal,
# et non pas si le fichier est importé comme module dans un autre script.
if __name__ == '__main__':
    main()