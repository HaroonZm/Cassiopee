W, H, N = map(int, input().split())
vertical_lines = set()
horizontal_lines = set()

for _ in range(N):
    A, B, C, D = map(int, input().split())
    if A == C:
        vertical_lines.add(A)
    else:
        horizontal_lines.add(B)

# On ajoute les bords du papier comme lignes de coupe
vertical_lines.add(0)
vertical_lines.add(W)
horizontal_lines.add(0)
horizontal_lines.add(H)

# Le nombre de parties est (nombre de segments verticaux) * (nombre de segments horizontaux)
vertical_lines = sorted(vertical_lines)
horizontal_lines = sorted(horizontal_lines)
ans = (len(vertical_lines)-1) * (len(horizontal_lines)-1)

print(ans)