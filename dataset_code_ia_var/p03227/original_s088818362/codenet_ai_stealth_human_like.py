# Bon, on lit la chaîne
t = input()
if len(t)==2:
    print(t)  # rien à faire dans ce cas, je suppose !
else:
    # Je retourne, c'est plus fun comme ça
    print(t[::-1])  # ouais, c'est bien comme ça