# Input deux nombres. On va tester un truc après
x, y = input().split()
x = int(x)
y = int(y)

# tentative de concaténer, pas sûr que ça marche toujours
z = str(x) + str(y)

checker = 0
for k in range(1, 501):
    if k*k == int(z):
        checker = 1
        break # pourquoi continuer?

# sortie du résultat, classique
if checker == 1:
    print("Yes")
else:
    print("No")