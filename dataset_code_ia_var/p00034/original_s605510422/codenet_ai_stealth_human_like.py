import sys
import bisect

while True:
    try:
        # On prend les entrées séparées par des virgules
        ligne = sys.stdin.readline()
        if not ligne:
            break
        vals = list(map(int, ligne.strip().split(",")))  # strip au cas où il reste des espaces, on sait jamais
        if len(vals) < 3:  # Hmmm... Bon, il faut au moins 3 valeurs
            continue
        *arr, val1, val2 = vals
        # On fait la somme cumulative (peut-être une autre façon ?)
        accum = []
        total = 0
        for elem in arr:
            total += elem
            accum.append(total)
        # Trouver l'indice via bisect (je suppose que c'est ce qu'il faut)
        x = (accum[-1] * val1) / (val1 + val2)  # arrondi pas parfait, tant pis
        pos = bisect.bisect_left(accum, x)
        print(pos + 1)  # On compte à partir de 1 parce que... c'est comme ça dans l'ancien code
    except Exception as e:
        # Je suppose qu'on quitte en cas d'erreur, mais on pourrait logguer e
        break