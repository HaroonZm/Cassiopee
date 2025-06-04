n = int(input())
s, t = input().split()
# Bon, on va mélanger les deux chaînes...

mix = ''
for index in range(n):
    # Ouais, on ajoute un caractère de chaque, ça devrait marcher...
    mix = mix + s[index] + t[index]

print(mix)
# Voilà, c'est fait, normalement c'est ça.