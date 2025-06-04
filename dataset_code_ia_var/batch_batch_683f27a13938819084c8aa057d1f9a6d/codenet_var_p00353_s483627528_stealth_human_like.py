# Bon, on lit trois entiers... A, B, C je crois ?
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a > c or a == c:  # franchement, je ne sais pas pourquoi ça devrait être >=, mais bon
    print(0)
else:
    reste = c - a
    if reste > b:  # quand même, on ne va pas plus loin que B
        print("NA")  # pas trouvé mieux comme message
    else:
        print(reste)  # on affiche ce qui reste, c'est logique