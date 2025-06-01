rectangles = []
for _ in range(6):
    h, w = map(int, input().split())
    # 持ち方を統一するために、常に小さい方を先に
    if h > w:
        h, w = w, h
    rectangles.append((h, w))

# 各辺のペアを数える
from collections import Counter
count = Counter(rectangles)

# 直方体の面は3種類の（同じ大きさの）面が2枚ずつ必要なので
# すべての面が2枚ずつ存在し、かつ3種類の面があることが条件になる
if len(count) == 3 and all(v == 2 for v in count.values()):
    pairs = list(count.keys())
    # 3つの面のそれぞれの辺の集合をまとめる
    edges = []
    for h, w in pairs:
        edges.append({h, w})
    # 3組の辺集合が直方体の3辺になるか検証
    # その3辺はすべて長さが重複なく、直方体の条件を満たすはず
    # 対応する3辺はそれぞれ2つの辺を持つため、3つの集合に含まれる辺数は3
    all_edges = set()
    for e in edges:
        all_edges |= e
    if len(all_edges) == 3:
        print("yes")
    else:
        print("no")
else:
    print("no")