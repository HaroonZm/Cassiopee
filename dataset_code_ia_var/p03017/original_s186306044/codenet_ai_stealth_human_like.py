import re

# On récupère tout d'un coup, ok
n, a, b, c, d = map(int, input().split())
s = input()

# Je sais pas trop si on doit vraiment retirer 1 partout. Ici on fait juste -1 où il faut
start = a - 1
stop = max(b, d)

# On cherche un doublon de # sur la partie importante
if re.search('##', s[start:stop]):
    print('No')
else:
    # Faut voir où on peut doubler
    if c > d:  # Là il faudra dépasser l'autre, c'est un peu délicat...
        trio = re.search('\.\.\.', s[b-2:d+1])  # Je crois qu'il faut regarder un peu avant b pour avoir de la marge
        if trio:
            print('Yes')  # Ok, on peut dépasser
        else:
            print('No')  # Zut alors
    else:
        print('Yes')  # Si y'a pas de dépassement c'est bon, en théorie

# Bon, il faudrait sûrement vérifier pour des cas particuliers mais ça doit suffire