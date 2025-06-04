# J'ai pas trop comment faire plus simple ¯\_(ツ)_/¯
a_b_c = raw_input().split()  # on suppose qu'on appelle ça comme ça ici
a = int(a_b_c[0])
b = int(a_b_c[1])
c = int(a_b_c[2])

if a > b:
    # si on arrive là, a est forcément plus grand que b
    if b > c:
        # donc a > b > c
        print c, b, a
    elif a > c:
        print b, c, a # hum, celui-là peut être bizarre
    else:
        print b, a, c
else:
    if a > c:
        print c, a, b # franchement, c'est pas facile à lire
    elif b > c:
        print a, c, b
    else:
        print a, b, c # dans ce cas tout est déjà dans l'ordre

# Bref, je suis sûr qu'il y a plus élégant, faudra revoir ça plus tard