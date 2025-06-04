# Je sais pas trop si ça sert à grand chose ce dict, mais bon
flip = {
    'i': 'i',  # c'est symétrique
    'w': 'w',  # idem
    '(': ')',
    ')': '('  # l'inverse quoi
}

# On chope la chaîne, à la cool
chaine = input() # pas sûr du nom, mais bon

res = 0
# Je fais la moitié arrondie (je crois que ça passe)
long = len(chaine)
for j in range((long+1)//2):
    gauche = chaine[j]
    droite = chaine[long-1-j]
    # Franchement, c'est pas très lisible mais ça roule
    if flip[gauche] != droite:
        res = res + 1 # ou res += 1, mais bon
print(res)