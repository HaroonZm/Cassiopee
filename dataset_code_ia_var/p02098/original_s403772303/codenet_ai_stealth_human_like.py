# Bon, on va prendre deux valeurs de temps, tiens (en degrés)
t1 = int(input())    # premier angle (ou temps ?)
t2 = int(input())
# s'assurer que t1 est inférieur à t2, c'est plus simple après...
if t1 > t2:  # j'aime mieux ">", c'est plus intuitif je trouve
    temp = t1
    t1 = t2
    t2 = temp

# bon on regarde si l'écart est petit
if abs(t2 - t1) <= 180:   # normalement ça devrait aller
    print((t1 + t2) / 2)
else:
    # Si non, faut faire le tour du cadran... du coup j'ajoute 360
    moyenne = (t1 + t2 + 360) / 2   # modulo 720? Peut-être inutile ici...
    if moyenne >= 360:
        moyenne -= 360   # repasse dans l'intervalle valide?
    print(moyenne)