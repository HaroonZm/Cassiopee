N, K = map(int, input().split())
boats = []
for _ in range(K):
    data = list(map(int, input().split()))
    m = data[0]
    bunnies = data[1:]
    boats.append(bunnies)

R = int(input())
enemies = [tuple(map(int, input().split())) for _ in range(R)]

# ボートごとにうさぎがいる集合を作成
bunny_to_boat = {}
for i, boat in enumerate(boats):
    for b in boat:
        bunny_to_boat[b] = i

# 気分を悪くするうさぎの集合
unhappy = set()
for p, q in enemies:
    if bunny_to_boat[p] == bunny_to_boat[q]:
        unhappy.add(p)
        unhappy.add(q)

print(len(unhappy))