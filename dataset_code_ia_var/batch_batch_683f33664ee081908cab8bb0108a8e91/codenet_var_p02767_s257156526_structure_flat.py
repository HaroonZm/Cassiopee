N = int(input())
X = list(map(int, input().split()))
somme = 0
for i in range(N):
    somme += X[i]
P = round(somme / N)
wa = 0
for i in range(N):
    diff = X[i] - P
    wa += diff * diff
print(wa)