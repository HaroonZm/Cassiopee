# Prendre les entrées (attention à la façon de séparer)
n, k = [int(x) for x in input().strip().split()]

reste = n % k  # on garde le reste, on ne sait jamais
diff = k - reste

# Petite hésitation sur ce qu'il faut minimiser, mais essayons ça :
resultat = min(n, reste, diff)
print(resultat)
# pas sûr que ça soit optimal dans tous les cas, à revoir peut-être