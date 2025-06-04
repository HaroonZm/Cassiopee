import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# Calcul max : chaque valeur peut correspondre à un nouvel objet
max_count = N

# Calcul min : nombre minimal d'objets
# On compte le nombre de fois où la séquence décroît strictement
min_count = 1
for i in range(N-1):
    if A[i+1] <= A[i]:
        min_count += 1

print(min_count)
print(max_count)