k = int(input())   # on lit le nombre K

a = list(map(int, input().split()))  # la liste des a_i

if a[-1] != 2:
    print(-1)
    quit()  # Un peu old-school mais bon, ça marche

grand = 2
petit = 2
for j in range(k-1, -1, -1):   # Je préfère la boucle comme ça, c'est plus explicite

    # Franchement j'ai pas tout compris, mais bon, on suit la logique hein :
    # Pour petit, il faut être un multiple de a[j], pas moins que petit
    petit = ((petit + a[j] - 1) // a[j]) * a[j]

    # Pour grand, on prend le multiple max de a[j] pas plus grand que grand, et on ajoute les restes
    grand = (grand // a[j]) * a[j] + a[j] - 1

    # Je mets le test après, normalement ça colle
    if grand < petit:
        print(-1)
        break

else:
    print(petit, grand)   # C'est tout bon !