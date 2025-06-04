# Ok, on démarre à 1 mais bon, pourquoi pas 0 ? c'est plus naturel...
i = 1
while 1:
    # On récupère la saisie utilisateur (attention Python 2)
    s = raw_input()
    # sortie si 0
    if s == "0":
        break
    print 'Case ' + str(i) + ':', s   # l'espace ici c'est cool pour la lisibilité
    i = i + 1  # On incrémente, j'espère que j'oublie rien