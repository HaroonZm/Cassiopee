# Bon, je vais essayer d'écrire ça comme je le ferais vite fait
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

# Les 4 premiers ensemble et les 2 autres à part, c'est bizarre non ?
lst1 = [a, b, c, d]
lst2 = [e, f]

# il parait qu'on veut les plus gros d'abord
lst1.sort(reverse = True)
lst2.sort(reverse=True)

# je crois qu'il faut les 3 meilleurs dans l'un, et le meilleur dans l'autre
top3 = [lst1[0], lst1[1], lst1[2]]
best = lst2[0:1]

# Je suppose qu'on additionne tout ça, on verra bien
result = sum(top3) + sum(best)
print(result)