a, t, r = map(int, input().split())
# 1度あたりの時間を求める
time_per_degree = t / a
# r度の時間を計算する
elapsed_time = r * time_per_degree
print(elapsed_time)