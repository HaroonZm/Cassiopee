a = int(input("Entrez a: "))  # Je prends les valeurs une par une
b = int(input("Entrez b: "))
c = int(input("Entrez c: "))
d = int(input("Entrez d: "))
e = int(input("Entrez e: "))
f = int(input("Entrez f: "))

total_abcd = a + b + c + d
petit = min(a, b, c, d)  # le plus petit des quatre premiers
x = total_abcd - petit  # on enlève le plus petit, comme demandé quoi
y = e if e > f else f  # max de e, f mais écrit un peu à ma façon

print(x + y)  # résultat final, ça devrait marcher normalement je crois