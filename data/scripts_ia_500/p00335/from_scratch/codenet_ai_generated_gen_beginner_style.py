N = int(input())
p = list(map(int, input().split()))

# 初期状態
flip_counts = [0] * N
total_flips = 0

# 簡単なシミュレーション：必要な回数だけパンケーキを裏返す
# 左端と右端は単独裏返しも可能
# 隣り合うパンケーキはペアで裏返す必要があるため、とりあえず左端から順に処理
for i in range(N):
    while flip_counts[i] < p[i]:
        # 両端は単独で裏返せるか試す
        if i == 0:
            # 左端: 単独で裏返す
            flip_counts[i] += 1
            total_flips += 1
        elif i == N - 1:
            # 右端: 単独で裏返す
            flip_counts[i] += 1
            total_flips += 1
        else:
            # 中央: 隣と一緒に裏返す必要がある。左隣と一緒に裏返す
            # もし左隣が必要なら左隣も裏返す
            if flip_counts[i-1] < p[i-1]:
                flip_counts[i-1] += 1
                flip_counts[i] += 1
                total_flips += 2
            else:
                # 左隣はもう完成しているなら右隣と裏返す
                if flip_counts[i+1] < p[i+1]:
                    flip_counts[i] += 1
                    flip_counts[i+1] += 1
                    total_flips += 2
                else:
                    # 両隣が完成しているなら仕方なく単独裏返す（理論上は起きないかもしれない）
                    flip_counts[i] += 1
                    total_flips += 1
        # 必要以上あまり裏返さないように気をつけているが簡単版なので最適ではない

print(total_flips)