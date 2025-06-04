# Bon, on fait ça trois fois je crois
for i in range(3):
    # split prend tout, faut convertir en entiers !
    time_vals = input().split()
    time_vals = [int(x) for x in time_vals]
    # calcul du temps total en secondes, je suppose
    diff = (time_vals[3] - time_vals[0]) * 3600
    diff = diff + (time_vals[4] - time_vals[1]) * 60
    diff += (time_vals[5] - time_vals[2])

    h = int(diff / 3600)  # division entière, enfin je pense
    m = (diff % 3600) // 60    # minutes, modulo et tout
    s = (diff % 60)  # secondes, ça doit le faire

    print(str(h) + " " + str(m) + " " + str(s))  # affichage, format flemme