premier_nombre, deuxieme_nombre = map(int, input().split())

est_divisible = (deuxieme_nombre % premier_nombre == 0)

if est_divisible:
    resultat = premier_nombre + deuxieme_nombre
else:
    resultat = deuxieme_nombre - premier_nombre

print(resultat)