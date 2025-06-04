# Bon, on va faire une petite boucle pour 3 essais je crois
for turn in range(3):
    data = input().split()
    h = int(data[0])
    m = int(data[1]); s = int(data[2])
    nh = int(data[3]); nm = int(data[4])
    ns = int(data[5]) # J'espère qu'il n'y a pas d'erreur ici

    # Calcul du nombre total de secondes avant/après
    start_sec = h*3600 + m*60 + s
    end_sec = nh*3600 + nm*60 + ns
    diff = end_sec - start_sec
    # ok bon, maintenant on refait le découpage
    hours = diff // 3600
    mins = (diff % 3600)//60
    secs = diff%60

    # Affiche le résultat, tant pis pour le format joli
    print(hours, mins, secs)