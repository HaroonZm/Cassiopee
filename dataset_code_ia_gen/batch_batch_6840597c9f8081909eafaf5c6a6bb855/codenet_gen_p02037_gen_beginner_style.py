h, w = map(int, input().split())
a, b = map(int, input().split())

# 壁の縦横それぞれにタイルの縦横が収まる個数を求める（タイルの向きは変えない）
tiles_vertical = h // a
tiles_horizontal = w // b

# 貼れるタイルの総数
total_tiles = tiles_vertical * tiles_horizontal

# タイルが覆う面積
covered_area = total_tiles * a * b

# 壁の面積
wall_area = h * w

# 覆われていない面積を求める
uncovered_area = wall_area - covered_area

print(uncovered_area)