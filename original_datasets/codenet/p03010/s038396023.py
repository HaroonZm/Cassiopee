from itertools import combinations, permutations

N = int(input())

# 整数列の生成
# s = [1]
# while len(s) < 10 :
    # i = s[-1] + 1
    
    # while True :
        # path = s.copy() + [i]
        # flag = True
        # for comb in combinations(s + [i], 2) :
            # if not sum(comb) in path :
                # path.append(sum(comb))
            # else :
                # flag = False
                # break
        # if flag :
            # s.append(i)
            # break
        # else :
            # i += 1
            
s = [1, 2, 4, 7, 12, 20, 29, 38, 52, 73]

w = [[0] * 10 for _ in range(10)]
w[0][1] = w[1][0] = 1

for n in range(3, N + 1) :
    # 最長経路探索
    M = 0
    for perm in permutations(range(n-1), n-1) :
        tmp = 0
        for i in range(n-2) :
            tmp += w[perm[i]][perm[i+1]]
        M = max(M, tmp)
    
    M += 1
    
    # 新規割当
    for i in range(n-1) :
        w[i][n-1] = w[n-1][i] = M * s[i]
        
        
for i in range(N) :
    print(' '.join([str(j) for j in w[i][:N]]))