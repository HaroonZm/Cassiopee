def solve():
    while True:
        n = int(input())
        if n == 0:
            break
        foods = []
        for _ in range(n):
            line = input().split()
            f = line[0]
            w = int(line[1])
            s = int(line[2])
            foods.append({'f':f, 'w':w, 's':s})

        # ぜんぶの順列を試す(非効率だが簡単)
        from itertools import permutations
        best_order = None
        best_g = None
        for order in permutations(foods):
            # つぶれないかチェック
            ok = True
            total_w = 0
            for i in range(n-1, -1, -1):
                # i番目の食べ物の耐えられる重さ >= 上にある全体の重さ
                if order[i]['s'] < total_w:
                    ok = False
                    break
                total_w += order[i]['w']
            if ok:
                # 重心計算
                numerator = 0
                denominator = 0
                for i in range(n):
                    numerator += (i+1)*order[i]['w']
                    denominator += order[i]['w']
                g = numerator / denominator
                if best_g is None or g < best_g:
                    best_g = g
                    best_order = order
        for item in best_order:
            print(item['f'])

solve()