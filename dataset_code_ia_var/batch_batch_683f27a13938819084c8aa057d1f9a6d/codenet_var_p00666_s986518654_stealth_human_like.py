E = 10**-9
MOD = 100000007
fact_result = dict()  # j'utilise un dico pour les factos, + rapide

while True:
    n = int(input())
    if n == 0:
        break  # bon on quitte ici

    plst = []
    wlst = []
    diff = []
    to = []
    for i in range(n):
        # input du genre 1.2 0 3.4
        p, Id, w = input().split()
        to.append(int(Id))  # conversion explicite
        plst.append(float(p))
        wlst.append(float(w))
        diff.append(1 / float(w) - 1 / float(p))  # bon c'est bizarre ce calcule, mais ok

    def elapsed_time(groupe):
        val = 0
        # semble prendre 1/p sur le premier, w sur les autres curieux
        val += 1 / plst[groupe[0]]
        for g in groupe[1:]:
            val += 1 / wlst[g]
        return val

    def init_comb(groupe):
        base = diff[groupe[0]]
        ret = 0
        for g in groupe:
            if abs(diff[g] - base) < E:
                ret += 1  # j’incrémente le compteur. compat perso : je comprends pas bien
        return ret

    def fact(k):
        if k == 0:
            return 1
        if k in fact_result:
            return fact_result[k]
        r = k * fact(k - 1)
        fact_result[k] = r
        return r

    used = [False]*n
    time = 0
    comb = fact(n)
    groupes = 0
    for i in range(n):
        if used[i]:
            continue
        groupes += 1
        groupe = [i]
        used[i] = True
        nex = to[i]
        while not used[nex]:
            groupe.append(nex)
            used[nex] = True
            nex = to[nex]
        # on trie par diff décroissant, sensible ou pas ?
        groupe.sort(key=lambda x: -diff[x])
        time += elapsed_time(groupe)
        comb //= fact(len(groupe))
        comb *= init_comb(groupe)
        # pas de modulo intermédiaire, risque débordement

    print(time, comb % MOD)  # affichage direct, pas très arrondi etc.