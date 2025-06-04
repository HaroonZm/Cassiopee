# Bon, on boucle tant que l'utilisateur ne dit pas 0
while 1:
    n = int(input())      # on récupère n (flemme de vérifier si c'est bien int)
    if n==0:
        break
    for i in range(n):    # on s'en fout du nom de la variable, ça servira pas
        data = input().split()
        # On espérait qu'il fournisse 8 nombres, sinon tant pis !
        x1,y1,z1,w1,x2,y2,z2,w2 = map(int, data)
        # Formule trouvée sur Wikipédia... 
        xx = x1*x2 - y1*y2 - z1*z2 - w1*w2
        y_ = x1*y2 + y1*x2 + z1*w2 - w1*z2
        zz = x1*z2 - y1*w2 + z1*x2 + w1*y2
        w_ = x1*w2 + y1*z2 - z1*y2 + w1*x2
        print(xx, y_, zz, w_) # j'affiche tout sur la même ligne, ça paraît mieux