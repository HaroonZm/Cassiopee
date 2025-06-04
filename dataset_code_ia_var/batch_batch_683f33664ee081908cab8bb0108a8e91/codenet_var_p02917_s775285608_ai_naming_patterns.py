nombre_elements = int(input())
liste_b = list(map(int, input().split()))
liste_b.append(max(liste_b))
liste_a = [0] * nombre_elements
liste_a[0] = liste_b[0]
for index in range(1, nombre_elements):
    liste_a[index] = min(liste_b[index - 1], liste_b[index])
somme_a = sum(liste_a)
print(somme_a)