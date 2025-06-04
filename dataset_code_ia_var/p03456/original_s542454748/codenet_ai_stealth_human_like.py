# Bon, on prend deux nombres
a, b = input().split()
a = int(a)
b = int(b)
# je concatène en string puis en int... pas sûr que ce soit optimisé, mais ça marche
n = int(str(a) + str(b))
m = "No"

for j in range(1, 999):  # Pourquoi 999? ça devrait suffire.
    if j * j == n:
        m = "Yes"
        # franchement, on pourrait break ici mais bon...
print(m)