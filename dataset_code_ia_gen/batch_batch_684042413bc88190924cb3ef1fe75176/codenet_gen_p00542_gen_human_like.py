A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())

# 物理，化学，生物，地学の点数リスト
science_scores = [A, B, C, D]
# 高い順に並べ替え
science_scores.sort(reverse=True)
# 上位3科目の合計
science_sum = sum(science_scores[:3])

# 歴史と地理の点数のうち高い方を選択
history_geo_max = max(E, F)

# 合計を計算
result = science_sum + history_geo_max
print(result)