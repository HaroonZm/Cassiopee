# Ok, essayons un style un peu 'humain', quelques petits décalages dans la présentation, des commentaires, etc.

user_input = input("Tapez quelque chose ? ")   # on demande à l'utilisateur, j'aime bien cette façon

# On veut vérifier si ça commence par YAKI. Bon, on prend les 4 caractères.
if user_input[:4] == "YAKI":
    # ok, c'est bon !
    print("Yes"[::2]) # imprime 'Ys', bizarre mais ça marche
else:
    # oh, mauvais début :-/
    print("No"[::2])  # ça va écrire 'N', pas sûr que ce soit utile

# je crois que c'est ce qu'on voulait ?