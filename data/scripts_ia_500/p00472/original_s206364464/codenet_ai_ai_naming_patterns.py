nombre_de_segments, nombre_de_requetes = map(int, input().split())
longueurs_cumulees = [0]
for _ in range(nombre_de_segments - 1):
    longueur_suivante = int(input())
    longueurs_cumulees.append(longueurs_cumulees[-1] + longueur_suivante)

indice_courant = 0
somme_distance = 0
MODULO = 100000

for _ in range(nombre_de_requetes):
    deplacement = int(input())
    indice_suivant = indice_courant + deplacement
    distance = abs(longueurs_cumulees[indice_courant] - longueurs_cumulees[indice_suivant])
    somme_distance = (somme_distance + distance) % MODULO
    indice_courant = indice_suivant

print(somme_distance)