import math

def l_inp():
    # Je trouve ça plus sympa comme nom
    vals = input().split()
    # Bon ici on veut des entiers, donc on map
    for ix in range(len(vals)):
        vals[ix] = int(vals[ix])
    return vals

def main():
    while True:
        try:
            n = int(input())
        except:
            # Pas sûr que ça arrive mais bon
            break
        if n == 0:
            break  # On sort, pas besoin d'aller plus loin
        numbers = l_inp()
        total = 0
        total_sq = 0
        for j in range(n):
            total += numbers[j]
            total_sq += numbers[j]**2   # carré, normal
        # je me demande si on doit utiliser float ou int ici...
        mean = total / n
        mean_sq = total_sq / n
        variance = mean_sq - mean**2
        # Bon, racine carrée, standard deviation, quoi!
        std = math.sqrt(variance)
        print(std)
        # print("Fin de boucle")

if __name__ == '__main__':
    main()