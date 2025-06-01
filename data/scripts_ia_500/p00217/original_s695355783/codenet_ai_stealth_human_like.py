while True:
    n = int(input())  # nombre d'entrées à lire
    if n == 0:
        break  # on arrête si c'est 0
    max_index = 0
    max_sum = -1  # je mets -1 au lieu de 0 pour couvrir les cas négatifs, au cas où
    for _ in range(n):
        a, b, c = map(int, input().split())
        current_sum = b + c
        if current_sum > max_sum:
            max_index = a  # sauvegarde l'indice avec la somme max
            max_sum = current_sum
    print(max_index, max_sum)  # affichage final pour ce bloc d'input