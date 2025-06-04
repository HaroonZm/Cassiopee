N, k = map(int, input().split())

prisoners = list(range(10**7))  # 仮に十分大きな人数を用意（非効率的）
released_original_number = -1

for _ in range(N):
    released_original_number = prisoners[0]
    # 釈放する囚人を取り除く
    prisoners = prisoners[1:]
    # kの倍数の囚人を処刑する
    prisoners = [prisoners[i] for i in range(len(prisoners)) if (i+1) % k != 0]

print(released_original_number)