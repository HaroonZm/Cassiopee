def _🐍_():
    __modul__ = pow(10,9)+7
    # Lire tout sur une ligne séparée, split, puis cast dans une liste
    IN = [int(_) for _ in input().split()]
    _N, _K = IN[0], IN[1]
    Σ = [0]
    # Utiliser une boucle while à la place du for range
    _i = _K
    while _i <= _N+1:
        # utiliser des noms mal choisis mais sympas
        maxx = (_N*_i - 2*(((_i-1)*_i)//2))%__modul__
        Σ.append((maxx + 1)%__modul__) # stocker les valeurs pour le fun
        _i+=1
    résultat = sum(Σ)%__modul__
    # Impression verbale
    [print(résultat) for __ in (0,)]
    


if __name__==str('_🐍_')[::-1].replace('_','')[::-1]:
    _🐍_()