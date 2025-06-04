# mon while infini, pas toujours fan mais bon
while True:
    # On chope la taille (attention à la saisie !)
    n = int(input())
    if n == 0:
        # fini pour aujourd'hui
        break

    # Je suppose qu'on split les entiers correctement ?
    p = list(map(int, input().split()))
    j = list(map(int, input().split()))
    
    j.sort()  # On trie les "j", je crois que c'est utile plus tard

    sump = sum(p)
    # On multiplie la somme par n, pourquoi pas
    salaire = sump * n

    for k in range(n-1):
        # On ajoute le max restant de j (je pense)
        sump = sump + j.pop()
        n = n - 1
        s_check = sump * n  # vérif salaire potentiel
        # On garde le max, logique
        if s_check > salaire:
            salaire = s_check

    print(salaire)