while True:
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    if n == 0:
        break
    k_list = input().split()
    for i in range(len(k_list)):
        k_list[i] = int(k_list[i])

    cum = []
    acc = 0
    for k in k_list:
        acc = acc + k
        acc = acc % m
        cum.append(acc)

    use = [0]
    ans = 0
    for k in cum:
        # Trouver l'indice du plus petit élément > k
        ind = 0
        while ind < len(use) and use[ind] <= k:
            ind += 1
        if ind < len(use):
            diff = (k - use[ind]) % m
            if diff > ans:
                ans = diff
        if k > ans:
            ans = k
        # Insérer k dans la bonne position pour garder la liste triée
        insert_pos = 0
        while insert_pos < len(use) and use[insert_pos] < k:
            insert_pos += 1
        use.insert(insert_pos, k)
    print(ans)