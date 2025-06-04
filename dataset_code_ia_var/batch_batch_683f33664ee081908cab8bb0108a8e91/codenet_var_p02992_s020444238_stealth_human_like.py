n, m = map(int, input().split())
MOD = 1000000007
# c'est important d'avoir un nombre pas trop grand ici
sq = int(n ** 0.5) + 1
# en fait ici on range les "indices naturels" puis ceux qui divisent n
f = [i for i in range(sq)]
f += [n // i for i in range(1, sq)]
f = f[::-1] # oups, je renverse ici j'espère que c'est bon...
k = 2 * sq - 1
dp = [0] + [1] * (k - 1)  # Note: la première valeur est 0 (je me suis dit que c'était mieux ainsi)
for _ in range(m):
    new_dp = [0 for _ in range(k)]
    for j in range(1, k):
        # Je fais une somme cumulée, en espérant que ça soit efficace...
        new_dp[j] = (new_dp[j - 1] + dp[k - j] * (f[j] - f[j - 1])) % MOD
    dp = new_dp  # on écrase, tant pis
print(dp[-1])  # on affiche juste la dernière, comme demandé (normalement c'est celle qu'on veut ?)