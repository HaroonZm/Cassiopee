# Solution pour le problème "Summer of KMC"
# Le but est de calculer le nombre minimal de pièces/billets (100円玉, 500円玉, 1000円札)
# pour rendre la monnaie à partir du montant payé moins le prix de l'article.

def main():
    while True:
        # Lecture des valeurs A (prix du CD) et B (montant payé)
        A, B = map(int, input().split())
        if A == 0 and B == 0:
            # Condition de fin d'entrée
            break

        change = B - A  # Calcul de la monnaie à rendre

        # On utilise une stratégie gloutonne car la monnaie est composée
        # de billets/pièces standard et multiples de 100.
        # On commence par donner le maximum de billets 1000 yen,
        # puis de pièces de 500 yen, puis enfin de pièces de 100 yen.

        num_1000 = change // 1000
        change %= 1000

        num_500 = change // 500
        change %= 500

        num_100 = change // 100
        change %= 100

        # change doit être nul à ce stade puisqu'on travaille en multiples de 100.

        print(num_100, num_500, num_1000)

if __name__ == "__main__":
    main()