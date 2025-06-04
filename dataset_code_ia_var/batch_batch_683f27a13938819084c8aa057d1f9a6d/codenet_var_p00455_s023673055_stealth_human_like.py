# Bon, on va le refaire à ma façon :)
for i in range(3):
    vals = input().split()
    h1 = int(vals[0])
    m1 = int(vals[1]); s1 = int(vals[2])
    # On fait pareil pour le second horaire
    h2 = int(vals[3]); m2 = int(vals[4]); s2 = int(vals[5])
    t1 = h1*3600 + m1*60 + s1
    t2 = h2*3600 + m2*60 + s2
    diff = t2 - t1
    # ok, trouvons les heures, minutes, secondes
    hours = int(diff/3600)
    rem = diff % 3600
    minutes = rem // 60
    secondes = rem % 60
    print(hours, minutes, secondes) # Voilà, c'est presque pareil