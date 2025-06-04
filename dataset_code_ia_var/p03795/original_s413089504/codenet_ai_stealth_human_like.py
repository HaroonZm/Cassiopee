# J'ai mis des commentaires qui peuvent aider (ou pas)
n = int(input())  # on convertit ici direct, pratique !

# Calcul approximatif mais ça marche
valeur = 800 * n - 200 * (n // 15)  # je préfère les // pour diviser ici
print(valeur) # affichage direct, pas besoin de f-string cette fois