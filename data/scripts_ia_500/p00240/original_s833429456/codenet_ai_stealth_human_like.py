while True:
    n = int(input())
    if n == 0:
        break  # fin du programme quand n vaut 0
    y = float(input())
    best_id, best_value = -1, 0
    for _ in range(n):
        b, r, t = map(int, input().split())
        if t == 1:
            # simple intérêt
            m = y * (r / 100) + 1
        else:
            # intérêt composé
            m = (1 + r / 100) ** y
        if best_id < 0 or m >= best_value:
            best_id, best_value = b, m  # garde le meilleur
    print(best_id)  # affiche l'identifiant avec la meilleure valeur