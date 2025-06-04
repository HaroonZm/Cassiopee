# Définition d'une liste nommée 'coins' qui contient les valeurs de différentes pièces de monnaie.
# Chacune de ces valeurs représente le montant en unité monétaire (par exemple, centimes ou yen).
coins = [1, 5, 10, 50, 100, 500]

# La condition suivante vérifie si le script Python est exécuté directement 
# (c'est-à-dire, pas importé dans un autre fichier). 
if __name__ == "__main__":
    # Demande à l'utilisateur de saisir une entrée depuis le clavier.
    # input() lit toute la ligne entrée par l'utilisateur sous forme de chaîne de caractères.
    # split() découpe cette chaîne en une liste de sous-chaînes séparées par un espace.
    # map(int, ...) convertit chaque sous-chaîne en un entier.
    # list() convertit le map en une liste d'entiers.
    # Par exemple, si l'utilisateur tape '2 0 3 0 0 1', wallet contiendra [2, 0, 3, 0, 0, 1].
    wallet = list(map(int, input().split()))
    
    # Initialisation d'une variable nommée 'sum' (somme en anglais) à zéro.
    # Cette variable va accumuler la somme totale d'argent présente dans le portefeuille.
    sum = 0
    
    # Boucle for qui va itérer sur une séquence d'entiers allant de 0 à 5 inclus (au total 6 itérations).
    # Cette séquence correspond à chaque indice de la liste 'coins' et de la liste 'wallet'.
    for i in range(6):
        # À chaque itération, on multiplie le nombre de pièces du type i (wallet[i]) 
        # par la valeur de la pièce correspondante (coins[i]).
        # Le résultat est ajouté à la variable 'sum', qui garde en mémoire le total.
        sum += (coins[i] * wallet[i])

    # Vérifie si la somme totale obtenue est supérieure ou égale à 1000.
    # Si c'est le cas, alors l'expression 'sum >= 1000' est vraie : on affiche 1.
    # Sinon, l'expression est fausse : on affiche 0.
    # L'instruction print() affiche le résultat dans la console.
    print(1 if sum >= 1000 else 0)