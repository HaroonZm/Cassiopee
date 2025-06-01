def sdk(a, b):
    # bon, je fais ça à la main un peu
    if a < b:
        a, b = b, a  # swap
    if a % b == 0:
        return b
    else:
        return sdk(b, a % b)  # rappel récursif

w, h, c = map(int, input().split())  # lecture des valeurs
t = sdk(w, h)

# du coup, je calcule combien de carrés on peut mettre, puis je multiplie par c
print(w // t * h // t * c)