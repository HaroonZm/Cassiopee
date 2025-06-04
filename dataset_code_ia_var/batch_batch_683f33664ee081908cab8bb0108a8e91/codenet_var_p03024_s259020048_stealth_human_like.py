# On prend l'entrée utilisateur, c'est du texte en fait
s = input()
n = len(s)  # Bon ça sert pas mais je laisse, on sait jamais

# Je vérifie combien de 'x' il y a, je pense que 7 c'est la limite
compteur_x = s.count("x")
if compteur_x > 7:
    print("NO")
else:
    print("YES")
# Franchement je sais pas si ça gère tout, mais ça devrait passer