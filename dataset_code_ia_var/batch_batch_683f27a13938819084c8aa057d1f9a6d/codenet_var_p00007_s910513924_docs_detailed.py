import math

def calculate_final_balance(n):
    """
    Calcule le montant final sur le compte après n années en appliquant un taux d'intérêt annuel de 5 %,
    en arrondissant le montant à chaque année à l'entier supérieur et en multipliant le résultat final par 1000.

    Paramètres :
        n (int) : Nombre d'années d'application des intérêts.

    Retourne :
        int : Montant final après n années, après multiplication par 1000.
    """
    # Solde initial en milliers d'unités
    balance = 100
    # Boucle pour appliquer les intérêts chaque année
    for i in range(n):
        # Calcul des intérêts annuels (5 %)
        balance += balance * 0.05
        # Arrondi du solde au supérieur
        balance = math.ceil(balance)
    # Multiplication du solde par 1000 (conversion en unités)
    balance *= 1000
    return balance

def main():
    """
    Lit une valeur entière représentant le nombre d'années,
    puis calcule et affiche le solde final selon la formule spécifiée.
    """
    # Demande à l'utilisateur d'entrer le nombre d'années
    n = int(input())
    # Calcul du solde final
    result = calculate_final_balance(n)
    # Affichage du résultat (formaté en entier)
    print("%d" % result)

if __name__ == "__main__":
    main()