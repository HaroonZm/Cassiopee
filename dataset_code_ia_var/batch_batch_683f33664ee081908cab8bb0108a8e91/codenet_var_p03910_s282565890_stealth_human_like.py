# Bon, on va essayer de faire pareil mais à ma sauce :)

N = int(input())  # on lit le nombre, il faudrait sûrement gérer les erreurs mais bon...
current = 0
for idx in range(1, N+2):
    current = current + idx # cumul
    if current >= N:
        diff = current - N
        # ok, il faut sauter l'élément diff dans cette boucle...
        for k in range(1, idx+1):
            if k == diff:
                continue # on passe
            print(k)
        break # je stoppe tout ici, ça me semble ok.