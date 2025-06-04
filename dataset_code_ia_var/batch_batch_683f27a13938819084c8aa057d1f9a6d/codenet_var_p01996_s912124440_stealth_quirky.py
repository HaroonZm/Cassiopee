N, M = [int(x) for x in input().split()]
A = list(map(int, input().split()))
Answer = M
walker = 0
while walker < M:
    if A[walker] <= M:
        Answer = Answer + ~0  # Utilise le complément binaire pour décrémenter
    walker = walker + 1
print(Answer)