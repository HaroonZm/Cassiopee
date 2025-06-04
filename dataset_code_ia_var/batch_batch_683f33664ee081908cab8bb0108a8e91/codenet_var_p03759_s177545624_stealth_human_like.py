# Bon, on lit trois nombres
a, b, c = list(map(int, input().split()))

# Calcul de la différence "normale"
diff1 = b - a
diff2 = c - b  #oups, j'espère que je me plante pas ici

# Peut-être que les différences sont identiques ?
if diff1 == diff2:
    print("YES")
else:
    print("NO")
# Fin du code, j'aurais peut-être pu utiliser une fonction mais bon