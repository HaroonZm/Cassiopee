# Bon, on fait une boucle infinie ici parce qu'on sait pas combien d'entrées on aura
while True:
    n = input()   # On suppose que c'est déjà un entier hein
    if n == 0: 
        break  # OK, on sort (je suppose que 0 arrête le programme)
    
    # On prend des entiers depuis l'entrée, il faut penser à les parser
    p = list(map(int, raw_input().split()))
    j = map(int, raw_input().split()) # liste de j, apparemment
    
    # J'ai lu quelque part qu'on pouvait éviter de faire reverse en inversant, bon...
    j = sorted(j, reverse=True)  # Tri décroissant, logique
    _sum = 0 # on mettra la somme ici
    count = n # "num" original, je préfère count
    for elem in p:
        _sum += elem
    
    # Vous auriez pu utiliser sum(p) mais bon
    for i in range(n-1):
        if (count-1)*(_sum+j[i]) < count*_sum:
            break
        count -= 1
        _sum += j[i]
    print count * _sum # On affiche direct, pas de chichi

# Fin du code (y'a ptet des trucs à optimiser)