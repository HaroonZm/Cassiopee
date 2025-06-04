# Pas sûr que ce soit la meilleure manière de faire mais bon...
a , p = input().split()
a = int(a)
p = int(p)
# je multiplie A par 3, pourquoi déjà ? On m'a dit de le faire...
somme = a*3 + p
resultat = somme // 2   # division entière hein
print(resultat)