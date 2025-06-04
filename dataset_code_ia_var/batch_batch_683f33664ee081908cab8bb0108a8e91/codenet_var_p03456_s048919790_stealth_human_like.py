# bon ok, voilà ma version (je change un peu le style comme demandé)

def resolve():
    a, b = input().split()
    # concaténation et conversion (faut pas oublier)
    c = int(a + b)
    # racine carrée, je préfère utiliser ** pour changer
    x = c ** 0.5
    # pas sûr si c'est la meilleure manière mais bon...
    if x == int(x):
        print("Yes")
    else:
        # on affiche No sinon, classique
        print("No")

# appel un peu à l'arrache
resolve()