import sys

for line in sys.stdin:
    # ok, on va chercher JOI et IOI dans chaque tranche de 3 caractères
    s = 0
    # attention à bien prendre la bonne longueur, j'ai tendance à me tromper là
    for i in range(len(line)-2):
        if line[i:i+3] == "JOI":
            s += 1
        elif line[i:i+3] == "IOI":
            s += 1j  # j'utilise 1j pour comptabiliser IOI un peu bizarrement
    # pas sûr que ça soit très clair comme méthode mais ça marche
    print(int(s.real))
    print(int(s.imag))