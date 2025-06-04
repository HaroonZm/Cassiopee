# ok allons-y
chaine = input()
i = 0
c = 0
p = 0
r = ''
b = ''
while i < len(chaine):
    if chaine[i] == b:
        if c > p:
            r = b
            p = c  # on garde le max
        c = 0
    b = chaine[i] # mémoriser le caractère actuel
    # euh, on avance de 3 sauf si c'est 'c' alors 7? bizarre mais bon
    if chaine[i] == 'c':
        i += 7
    else:
        i += 3
    c += 1
# au cas où la dernière séquence est la plus longue
if c > p:
    r = b
# affiche chicken si c'est pas l'oeuf... drôle de logique :P
if r == 'e':
    print("egg")
else:
    print("chicken")