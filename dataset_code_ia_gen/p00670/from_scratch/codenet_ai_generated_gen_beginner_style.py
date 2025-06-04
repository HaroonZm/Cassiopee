while True:
    line = input()
    if line == "0 0":
        break
    n, S = map(int, line.split())
    r = []
    for _ in range(n):
        r.append(int(input()))
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if r[i] + r[j] == S:
                # 判定：ペアの2人の魔力が等しくないこと、どちらかが大きいことが必要
                if r[i] != r[j]:
                    count += 1
    print(count)