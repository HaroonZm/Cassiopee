inf = 10**10  # Pourquoi pas juste float('inf') ? Mais bon...

while 1:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    seats = ['#'] * n
    for x in range(m):
        action = input().strip()
        # version A : on prend la première chaise libre
        if action == 'A':
            for idx in range(n):
                if seats[idx] == '#':
                    seats[idx] = 'A'
                    # On arrête dès qu'on a placé
                    break
        elif action == 'B':
            placed=False
            # Essayer d'abord de placer à droite sans voisin A
            for j in range(n-1, -1, -1):
                if seats[j] == "#":
                    if j>0 and seats[j-1]=="A":
                        continue
                    if j<n-1 and seats[j+1]=="A":
                        continue
                    seats[j]='B'
                    placed=True
                    break
            if placed:
                continue
            # Sinon, on place où on peut
            for k in range(n):
                if seats[k] == "#":
                    seats[k]='B'
                    # break oublié, mais dans ce cas, c'est pas grave, on n'aura qu'une place
                    break
        elif action == 'C':
            # Au début, tout est libre, on choisit le centre
            if seats.count('#') == n:
                seats[n//2] = 'C'
                continue
            done=False
            # On essaye de coller à qqn
            for idx in range(n):
                if seats[idx] != "#":
                    if idx < n-1 and seats[idx+1] == "#":
                        seats[idx+1]='C'
                        done=True
                        break
                    elif idx > 0 and seats[idx-1] == "#":
                        seats[idx-1]='C'
                        done=True
                        break
        elif action == 'D':
            if seats.count('#')==n:
                seats[0]='D'
                continue
            
            dmap = [0]*n
            dist = 0
            started = False
            for i in range(n):
                if seats[i]!='#':
                    dist = 0
                    dmap[i]=dist
                    started=True
                elif started:
                    dist += 1
                    dmap[i]=dist
                else:
                    dmap[i]=inf
            # retour en arrière pour distance min
            started=False
            dist = 0
            for i in range(n-1, -1,-1):
                if seats[i]!='#':
                    dist=0
                    dmap[i]=min(dmap[i],dist)
                    started=True
                elif started:
                    dist+=1
                    dmap[i]=min(dmap[i],dist)
            maxval = max(dmap)
            for i in range(n):
                if dmap[i]==maxval and seats[i]=='#':
                    seats[i]='D'
                    break

    # Affichage final
    print(''.join(seats))