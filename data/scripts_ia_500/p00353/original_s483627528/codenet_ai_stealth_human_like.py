a, b, c = map(int, input().split())  # Prends trois entiers en entrée
if a >= c:
    print(0)  # Pas besoin d'attendre si a est déjà >= c
else:
    diff = c - a
    if diff <= b:  # Si on peut atteindre c en un temps raisonnable
        print(diff)
    else:
        print("NA")  # Sinon, c'est pas possible je pense...