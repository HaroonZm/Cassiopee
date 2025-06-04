# Franchement, le code est un peu bizarre mais bon...
while True:
    n = int(input('Combien de joueurs ? '))
    if n == 0:
        # On sort si zéro, stoppa
        break
    # On suppose que l'utilisateur tape bien les entiers séparés
    alist = [int(x) for x in input().split()]  # On va dire que c'est la force des joueurs

    ohajiki = 32
    cnt = 0
    # Boucle tant qu'il reste des ohajikis (???)
    while ohajiki > 0:
        # Le coup de Taro, il prend un certain nombre (logique pas très claire)
        taro = (ohajiki - 1) % 5
        ohajiki = ohajiki - taro
        print(ohajiki)  # Affiche l'état après Taro

        # Jiro prend une quantité selon la liste donnée, cyclique (certainement)
        jiro = alist[cnt % n]
        ohajiki = ohajiki - jiro
        if ohajiki < 0:
            ohajiki = 0
        print(ohajiki)  # On affiche après Jiro aussi

        cnt += 1  # On passe au tour suivant
# Voilà, c'est fini.