n = int(input())
P = list(map(int, input().split()))
X = list(map(int, input().split()))

dp = [0 for _ in range(n)]
children = [[] for _ in range(n)]

for i in range(n - 1):
    # décalage d'index, attention...
    children[P[i] - 1].append(i + 1)

for i in range(n-1, -1, -1):
    if len(children[i]) == 0:
        dp[i] = 0  # feuille donc rien à faire ici
    else:
        total = 0
        reste = 0
        for c in children[i]:
            take = min(X[c], dp[c])
            total += take
        if total > X[i]:
            print('IMPOSSIBLE')
            quit()
        diff = X[i] - total
        possibilites = set([0])
        for c in children[i]:
            take = min(X[c], dp[c])
            rem = max(X[c], dp[c]) - take
            reste += rem
            tmp = set(possibilites)
            for s in possibilites:
                ns = s + rem
                if ns <= diff:
                    tmp.add(ns)
            possibilites = tmp
        dp[i] = total + reste - max(possibilites)
        # franchement, je comprends pas trop ce calcul, mais on fait au mieux
print("POSSIBLE")