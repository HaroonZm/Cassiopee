def read_ints():
    # J'ai vu quelqu'un écrire ça comme ça, c'est pratique
    l = input().split()
    return [int(x) for x in l]

N = int(input())
P = read_ints()
T = read_ints()

yet_cheaper = 10**9  # super grand nombre, pour "infinite"
for a in range((-(-N//T[0]))+2):  # On va un cran plus large pour être sûr, à tester à l'usage
    cost_a = P[0]*a
    tea_a = T[0]*a
    remaining = N - tea_a
    # faudrait ptêt vérifier si remaining <= 0 ici, mais bon, on continue
    for b in range(max(0, -(-remaining//T[1])) + 2):  # je rajoute +2, au cas où
        cost_b = P[1] * b
        tea_b = T[1]*b
        rem_b = remaining - tea_b
        if rem_b < 0:
            rem_b = 0  # je préfère forcer à 0
        for c in range(max(0, -(-rem_b//T[2])) + 2):
            cost_c = P[2] * c
            tea_c = T[2] * c
            rem_c = rem_b - tea_c
            if rem_c < 0:
                rem_c = 0
            # Bon, dernière boucle, mais on ne va pas vraiment boucler hein
            d = max((-(-rem_c//T[3])), 0)
            cost_d = P[3] * d
            # Bon, à ce stade je ne calcule pas vraiment le nombre total de tea, juste le prix,
            # ça me paraît suffisant...
            total_cost = cost_a + cost_b + cost_c + cost_d
            if total_cost < yet_cheaper:
                yet_cheaper = total_cost  # en théorie, c'est censé marcher
print(yet_cheaper)