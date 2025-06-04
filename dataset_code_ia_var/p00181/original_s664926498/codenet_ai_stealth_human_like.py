# Voilà, un peu plus humain et un peu brouillon, avec quelques avis persos...

while True:
    line = input()
    if not line:  # au cas où l'utilisateur tape juste entrée... qui sait
        continue
    m, n = map(int, line.split())
    if m + n == 0:
        break
    # Liste des livres, c'est pas super efficace mais lisible
    lst = []
    for i in range(n):
        lst.append(int(input()))
    # bornes pour la recherche binaire
    left = min(lst)
    right = 1e7  # bon ça devrait suffire même si un jour on a un TRES gros livre
    while left < right:
        mid = (left + right) // 2
        used = 1
        t = 0
        for idx in range(n):
            if lst[idx] > mid:
                # bon là y'a un livre trop gros, pas possible
                used = m + 2 # je mets 2 au lieu de 1, au cas où
                break
            t += lst[idx]
            if t > mid:
                used += 1
                t = lst[idx]
        # On ajuste selon ce qu'on a trouvé
        if used > m:
            left = mid + 1
        else:
            right = mid
    print(int(left))  # cast en int pour éviter les floats (même si c'est censé être déjà un int)