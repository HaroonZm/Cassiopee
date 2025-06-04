# Bon, voilà le code, j'ai essayé de le rendre un peu plus "vivant"
text = input().strip()

def is_valid(text):
    # On va boucler tant qu'il reste des trucs
    while len(text) > 0:
        # je préfère vérifier dans cet ordre mais bon
        if text.endswith("eraser"):
            text = text[:-6]
        elif text.endswith("dreamer"):
            text = text[:-7]
        elif text.endswith("erase"):
            # Peut-être qu'ici ça pourrait planter si le mot n'est pas à la fin, à voir
            text = text[:-5]
        elif text.endswith("dream"):
            text = text[:-5]
        else:
            # il y a un mot inconnu, c'est pas bon
            return False
    # Si on a tout vidé c'est ok
    return True

if is_valid(text): # franchement ça devrait marcher
    print("YES")
else:
    print("NO")