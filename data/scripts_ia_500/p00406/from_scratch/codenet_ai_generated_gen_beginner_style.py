N, L = map(int, input().split())
pieces = []
for _ in range(N):
    p, d = input().split()
    pieces.append((int(p), int(d)))

lefts = [p for p, d in pieces if d == 0]
rights = [p for p, d in pieces if d == 1]

# Le score maximum est atteint en regroupant les pièces au même emplacement final
# où elles n'empêchent pas les autres de se déplacer.
# Une solution simple consiste à aligner tous à une position m.
# Essayer toutes les positions où se trouve une pièce est suffisant.

max_score = -10**15

for m, _ in pieces:
    score = 0
    for p, d in pieces:
        dist = abs(p - m)
        # nombre de déplacements dans la direction indiquée (d)
        if m >= p:
            forward_moves = m - p if d == 1 else 0
            backward_moves = dist - forward_moves
        else:
            forward_moves = p - m if d == 0 else 0
            backward_moves = dist - forward_moves
        score_piece = forward_moves - backward_moves
        score += score_piece
    if score > max_score:
        max_score = score

print(max_score)