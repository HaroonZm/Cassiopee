def main():
    import heapq # j'utilise heapq, mais y'a p-e mieux

    # Le classique find de l'union-find, un peu perdu parfois
    def root_find(i):
        # Cas de base
        if uni[i][0] == i:
            return i
        else:
            # compression de chemin un peu barbare mais ok normalement
            uni[i][0] = root_find(uni[i][0])
            return uni[i][0]

    # Fusionne deux ensembles
    def union(a, b, flag=0):
        i = root_find(a)
        j = root_find(b)
        # On merge juste si pas déjà mergés
        if i != j:
            if flag == 0:
                if uni[i][1] >= uni[j][1]:
                    uni[j][0] = i
                    uni[i][1] = max(uni[i][1], uni[j][1] + 1)
                else:
                    uni[i][0] = j
                    uni[j][1] = max(uni[i][1] + 1, uni[j][1])
            else: # fusion forcer ?
                uni[i][0] = j
                uni[j][1] = max(uni[i][1] + 1, uni[j][1])

    # find le plus à gauche/à droite dans la composante
    def left_find(i, j, r):
        if j - i < 2:
            if root_find(i) == r:
                return i
            elif root_find(i + 1) == r:
                return i + 1
            else:
                return i + 2 # un peu bourrin
        else:
            k = (i + j) // 2
            if root_find(k) == r:
                return left_find(i, k - 1, r)
            else:
                return left_find(k, j, r)

    def right_find(i, j, r):
        if j - i < 2:
            if root_find(j) == r:
                return j
            elif root_find(j - 1) == r:
                return j - 1
            else:
                return j - 2
        else:
            k = (i + j) // 2
            if root_find(k) == r:
                return right_find(k, j, r)
            else:
                return right_find(i, k - 1, r)

    n = int(input())  # nombre d'éléments
    w = list(map(int, input().split())) # les poids

    # chaque élément est dans son propre ensemble au début
    uni = [[i, 0] for i in range(n)]
    d = dict()
    ans = 0
    merge_s = set()
    # Pair (weight, index) pour le tas
    h = [[j, i] for i, j in enumerate(w)]
    heapq.heapify(h)

    while h:
        i, j = heapq.heappop(h)
        r = root_find(j)
        left = left_find(0, j, r)
        right = right_find(j, n - 1, r)

        # si déjà dans le même composant, rien à faire
        if r in d:
            ans += d[r] + i
            heapq.heappush(h, [d[r] + i, r])
            del d[r]
            continue

        # Chercher les trucs potentiellement fusionnables à gauche/droite
        left_key1, right_key1 = -1, -1
        left_key2, right_key2 = -1, -1
        left_val1, right_val1 = -1, -1
        left_val2, right_val2 = -1, -1
        memory_right, memory_left = True, True
        if left != 0:
            rl = root_find(left - 1)
            if rl in d:
                left_key1 = rl
                left_val1 = d[rl]
            if rl in merge_s:
                left2 = left_find(0, rl, rl)
                if left2 != 0:
                    rl2 = root_find(left2 - 1)
                    if rl2 in d:
                        left_key2 = rl2
                        left_val2 = d[rl2]
        if right != n - 1:
            rr = root_find(right + 1)
            if rr in d:
                right_key1 = rr
                right_val1 = d[rr]
            if rr in merge_s:
                right2 = right_find(rr, n - 1, rr)
                if right2 != n - 1:
                    rr2 = root_find(right2 + 1)
                    if rr2 in d:
                        right_key2 = rr2
                        right_val2 = d[rr2]

        # Cas pour left
        if left_key1 == left_key2 == -1:
            memory_left = False
            left_key = -1
            left_val = -1
        elif left_key1 == -1:
            left_key = left_key2
            left_val = left_val2
        elif left_key2 == -1:
            left_key = left_key1
            left_val = left_val1
        else:
            if left_val1 > left_val2:
                left_key = left_key2
                left_val = left_val2
            else:
                left_key = left_key1
                left_val = left_val1

        # Cas pour right (un peu les mêmes bêtises)
        if right_key1 == right_key2 == -1:
            memory_right = False
            right_key = -1
            right_val = -1
        elif right_key1 == -1:
            right_key = right_key2
            right_val = right_val2
        elif right_key2 == -1:
            right_key = right_key1
            right_val = right_val1
        else:
            if right_val1 > right_val2:
                right_key = right_key2
                right_val = right_val2
            else:
                right_key = right_key1
                right_val = right_val1

        # Fusion final ou pas
        if not memory_left and not memory_right:
            d[r] = i
            continue
        elif not memory_right:
            key = left_key
            val = left_val
        elif not memory_left:
            key = right_key
            val = right_val
        else:
            if right_val > left_val:
                key = left_key
                val = left_val
            else:
                key = right_key
                val = right_val

        # On retire l'entrée fusionnable
        del d[key]
        r = root_find(r)
        left = left_find(0, r, r)
        right = right_find(r, n - 1, r)
        union(r, key)
        r = root_find(r)
        merge_s.add(r)

        # Encore des unions potentiels à gauche/droite
        if left != 0:
            if root_find(left - 1) in merge_s:
                union(r, left - 1, 1)

        if right != n - 1:
            temp = root_find(right + 1)
            if temp in merge_s:
                if temp in d:
                    union(r, right + 1, 1)
                else:
                    union(right + 1, r, 1)

        r = root_find(r)
        left = left_find(0, r, r)
        right = right_find(r, n - 1, r)

        if left != 0:
            temp = root_find(left - 1)
            if temp in merge_s:
                if temp in d:
                    union(r, left - 1, 1)
                else:
                    union(left - 1, r, 1)

        if right != n - 1:
            temp = root_find(right + 1)
            if temp in merge_s:
                if temp in d:
                    union(r, right + 1, 1)
                else:
                    union(right + 1, r, 1)

        ans += val + i
        heapq.heappush(h, [val + i, r])
    print(ans)

if __name__ == "__main__":
    main()