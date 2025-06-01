amount = 100000  # montant initial
n = int(input("Entrez le nombre d'itérations : "))  # nombre de fois à répéter

for _ in range(n):
    amount = amount * 1.05  # application d'une augmentation de 5%
    # j'ai essayé d'arrondir au millier supérieur sauf si c'est déjà pile
    if amount % 1000 != 0:
        amount = (amount + 1000) - (amount % 1000)
    # sinon, on laisse tel quel, pas besoin de faire quelque chose

print(int(amount))  # affichage final, sans décimales inutiles évidement