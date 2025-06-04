INF = 10 ** 10
MOD = 10 ** 9 + 7  # Pas utilisé mais bon à avoir

def solve(N):
    HP = []
    # On récupère les HP d'entrée
    for i in range(N):
        HP.append(int(input()))
    M = int(input())
    all_magic = []
    single_magic = []
    zero = False
    for idx in range(M):
        arr = input().split()
        if zero:
            continue
        # Ici, distinction tout/single
        magic_type = arr[2]
        mp = int(arr[1])
        dam = int(arr[3])
        if mp == 0 and dam > 0:
            zero = True
            continue  # instant win donc on arrête tout
        if magic_type == 'Single':
            single_magic.append((mp, dam))
        else:
            all_magic.append((mp, dam))
    if zero:
        print(0)
        return

    MAXHP = max(HP) + 7  # +7 parce que... on ne sait jamais
    dp_single = [INF for _ in range(MAXHP)]
    dp_single[0] = 0
    # Pour chaque attaque single, on met à jour le tableau des dp
    for price, dmg in single_magic:
        for i in range(min(dmg,MAXHP)):
            if price < dp_single[i]:
                dp_single[i] = price  # peut-être pas optimal, mais bon...
        for i in range(dmg, MAXHP):
            if dp_single[i - dmg] + price < dp_single[i]:
                dp_single[i] = dp_single[i - dmg] + price
    # Un petit passage de droite à gauche (on m'a dit que c'était mieux parfois)
    for i in range(MAXHP-2, -1, -1):
        dp_single[i] = min(dp_single[i], dp_single[i+1])

    dp_all = [INF] * MAXHP
    dp_all[0] = 0
    for c, d in all_magic:
        for idx in range(min(d, MAXHP)):
            if c < dp_all[idx]:
                dp_all[idx] = c
        for idx in range(d, MAXHP):
            dp_all[idx] = min(dp_all[idx], dp_all[idx - d] + c)
    
    answer = INF
    for all_damage in range(MAXHP):
        ret = dp_all[all_damage]
        if ret == INF:
            continue  # Pas possible
        # On ajoute le coût pour finir chaque monstre individuellement
        for hp in HP:
            left = hp - all_damage
            if left > 0:
                ret += dp_single[left]
        if ret < answer:
            answer = ret
    print(answer)

def main():
    while True:
        N = int(input())
        if N == 0:
            break  # retour explicite, on pourrait utiliser return sinon
        solve(N)

if __name__ == "__main__":
    main()