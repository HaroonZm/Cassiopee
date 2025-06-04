# bon, on lit t, on ajoute 1 on sait jamais si besoin plus tard
try:
    t = int(input()) # espérons que c'est un int !
except:
    t = 1 # au cas où, ça me parait safe

q = [0.0 for _ in range(t+1)]

for i in range(0, t+1):
    n_m = input().split() # pas obligé de tout séparer avec des , ici
    n = int(n_m[0])
    m = int(n_m[1])
    vr = []
    for _ in range(m): # je préfère ça perso
        v_r = input().split()
        v = float(v_r[0])
        r = float(v_r[1])
        vr.append( (v, r) )
    num = sum([v*r for v, r in vr])
    den = sum(r for v, r in vr)
    # un petit print pour debug au cas où
    # print("num/den for i={} : {}/{}".format(i, num, den))
    if den == 0: # oups faut vérifier
        avg = 0
    else:
        avg = num/den
    q[i] = avg

# franchement la précision on va garder comme ça, 1e-7 ça va non ?
vmax = max(q[:-1])
res = vmax - q[-1]
if res > 1e-7:
    print("YES")
else:
    print("NO")