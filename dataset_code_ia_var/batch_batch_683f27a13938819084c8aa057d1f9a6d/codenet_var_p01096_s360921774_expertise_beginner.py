def solve(n, lst):
    # On crée une table dp pour stocker les résultats
    dp = []
    for i in range(n + 1):
        line = []
        for j in range(n):
            line.append(0)
        dp.append(line)

    # Initialisation : pour chaque paire consécutive proche, on peut les prendre toutes les deux
    for j in range(n - 1):
        if abs(lst[j] - lst[j + 1]) <= 1:
            dp[2][j] = 2

    # On remplit dp
    for size in range(3, n + 1):
        for start in range(n - size + 1):
            max_value = 0
            if size % 2 == 0:
                # Cas où on peut associer le premier et le dernier
                if abs(lst[start] - lst[start + size - 1]) <= 1:
                    if dp[size - 2][start + 1] == size - 2:
                        dp[size][start] = size
                        continue
                # Sinon, on essaie de séparer le segment en deux parties
                max_value = dp[size - 2][start + 1]
                k = 2
                while k < size:
                    sum_parts = dp[k][start] + dp[size - k][start + k]
                    if max_value < sum_parts:
                        max_value = sum_parts
                    k += 2
            else:
                # Taille impaire, on essaie toutes les séparations possibles
                k = 1
                while k < size:
                    sum_parts = dp[k][start] + dp[size - k][start + k]
                    if max_value < sum_parts:
                        max_value = sum_parts
                    k += 2
            dp[size][start] = max_value
    print(dp[n][0])

while True:
    n = int(input())
    if n == 0:
        break
    lst = list(map(int, input().split()))
    solve(n, lst)