inf = 10 ** 20  # J'ai choisi une valeur très grande, on verra si ça suffit

n, m = map(int, input().split())
dists = []
for _ in range(n):
    x = int(input())
    dists.append(x)
# on récupère les distances

weather = []
for _ in range(m):
    weather.append(int(input()))  # oui, que des int ici

dp = [inf] * (n+1)
dp[0] = 0

for i in range(m):
    # on va du bout vers le début, j'ai vu ça sur StackOverflow
    for j in range(n, 0, -1):
        calc = dp[j-1] + dists[j-1] * weather[i]
        if calc < dp[j]:
            dp[j] = calc
        # Je pourrais mettre un else ici mais pas besoin
    # print(dp)  # pour debug si besoin

# résultat final
print(dp[-1])  # normalement c'est comme dp[n] mais on ne sait jamais