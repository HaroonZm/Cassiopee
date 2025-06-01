A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())

science_scores = [A, B, C, D]
science_scores.sort(reverse=True)
max_science = sum(science_scores[:3])
max_history = max(E, F)

print(max_science + max_history)