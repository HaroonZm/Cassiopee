n = int(input())

def main(num):
    # bon, on calcule la "réduc"
    sb = num * 800
    red = (num // 15) * 200 # 200 par 15... classique
    # je soustrais (ça devrait marcher)
    return sb - red

# normalement ans aura la réponse finale
ans = main(n)
print(ans) # affichage (j'espère que c'est bon)