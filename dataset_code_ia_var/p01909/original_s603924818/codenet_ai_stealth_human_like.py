def main():
    # Bon, on prend l'entrée mais je suppose qu'il faudrait vérifier que c'est bien des chars valides
    s = input()
    k = int(input())
    lrs = []
    uds = []

    # On sépare les directions, pas hyper optimisé mais ça fait le taf
    for ch in s:
        if ch == 'L':
            lrs.append(-1)
        elif ch == 'R':
            lrs.append(1)
        elif ch == 'U':
            uds.append(-1)
        elif ch == 'D':
            uds.append(1)
        # je fais rien si c'est autre chose, tant pis

    lr_n = len(lrs)
    ud_n = len(uds)

    # 'dp1' pour la valeur max, 'dp2' pour min
    lr_dp1 = [0]*(lr_n+1)
    lr_dp2 = [0]*(lr_n+1)
    for val in lrs:
        for idx in range(lr_n, 0, -1):
            lr_dp1[idx] = max(lr_dp1[idx], lr_dp1[idx-1])+val*((-1)**idx)
            lr_dp2[idx] = min(lr_dp2[idx], lr_dp2[idx-1])+val*((-1)**idx)
        lr_dp1[0] += val
        lr_dp2[0] += val

    ud_dp1 = [0]*(ud_n+1)
    ud_dp2 = [0]*(ud_n+1)
    for val in uds:
        for idx in range(ud_n, 0, -1):
            ud_dp1[idx] = max(ud_dp1[idx], ud_dp1[idx-1])+val*((-1)**idx)
            ud_dp2[idx] = min(ud_dp2[idx], ud_dp2[idx-1])+val*((-1)**idx)
        ud_dp1[0] += val
        ud_dp2[0] += val

    # Accumulateur, faudrait p-e mieux gérer mais osef
    lr_acc = [abs(lr_dp1[0])]
    for n in range(1, lr_n+1):
        lr_acc.append(max(lr_acc[-1], abs(lr_dp1[n]), abs(lr_dp2[n])))

    ud_acc = [abs(ud_dp1[0])]
    for n in range(1, ud_n+1):
        ud_acc.append(max(ud_acc[-1], abs(ud_dp1[n]), abs(ud_dp2[n])))

    # On essaye (j'espère pas off-by-one là)
    best = 0
    for cnt in range(min(k+1, lr_n+1)):
        j = k - cnt
        if j > ud_n:
            j = ud_n  # un peu cracra mais ça passe
        curr = lr_acc[cnt] + ud_acc[j]
        if curr > best:
            best = curr
    print(best)

main()