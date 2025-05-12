MAX_V = 999999999999999999999
while 1:
    n,m = list(map(int,input().split()))
    if n == 0:break
    costs = {x:[] for x in range(1,n+1)}
    passed = [[0 for x in range(2)] for y in range(n+1)]
    result = [MAX_V,MAX_V]
    for i in range(m):
        a,b,c = list(map(int,input().split()))
        costs[a].append((b,c))
        costs[b].append((a,c))

    spam = [(0,1,2)] #(cost,num,free tickets count)
    while len(spam) > 0:
        mc = min(spam)
        spam.remove(mc)

        tic_i = 0 if mc[2] == 2 else 1

        if mc[2] != 1 and passed[mc[1]][tic_i] != 0:
            continue

        if mc[2] != 1:
            passed[mc[1]][tic_i] = 1
            if n == mc[1]:
                result[tic_i] = mc[0]

        if max(result) < MAX_V:break

        #移動できる場所の登録
        for cv in costs[mc[1]]:
            #チケット不使用
            if mc[2] != 1:
                spam.append((mc[0] + cv[1],cv[0],mc[2]))
            #チケット使用
            if mc[2] > 0:
                spam.append((mc[0],cv[0],mc[2]-1))

    print(min(result))