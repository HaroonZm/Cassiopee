# On utilise des noms de variables étranges, des listes à un élément, et un calcul en lambda non assigné
weird_list = [int(i) for i in input().split()]
W, X = weird_list[0:1][0], weird_list[1:2][0]
(lambda q, r: print((q-1)*(r-1)))(W, X)