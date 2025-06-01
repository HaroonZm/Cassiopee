def lire_entree():
    return map(int, raw_input().split())

def somme_courante(cart, que, sp):
    sm = 0
    for num in range(8):
        valeur_cart = cart[(sp + num) % 8]
        if valeur_cart <= que[num]:
            sm += valeur_cart
        else:
            sm += que[num]
    return sm

def rotation_cart(cart, sp):
    return cart[sp:] + cart[:sp]

def convertir_rotations_en_chaine(cart_rotation):
    return "".join(map(str, cart_rotation))

def comparer_chaines(cart1, cart2):
    return int(cart1) > int(cart2)

def processeur_de_la_liste_eclipse(cart, que):
    mx = 0
    mxcart = "99999999"
    for sp in range(8):
        sm = somme_courante(cart, que, sp)
        cart_rotation = rotation_cart(cart, sp)
        acart = convertir_rotations_en_chaine(cart_rotation)
        if sm > mx:
            mx = sm
            mxcart = acart
        elif sm == mx:
            if comparer_chaines(mxcart, acart):
                mxcart = acart
    return mxcart

def afficher_resultat(mxcart):
    print " ".join(map(str, mxcart))

cart = [4,1,4,1,2,1,2,1]
while True:
    try:
        que = lire_entree()
        mxcart = processeur_de_la_liste_eclipse(cart, que)
        afficher_resultat(mxcart)
    except:
        break