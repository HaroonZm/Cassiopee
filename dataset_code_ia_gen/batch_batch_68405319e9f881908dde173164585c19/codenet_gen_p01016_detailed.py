# Lecture des entrées
A = input()
B = input()

# Longueur des chaînes
len_A = len(A)
len_B = len(B)

# On parcourt toutes les positions possibles dans A où B peut correspondre
for i in range(len_A - len_B + 1):
    match = True  # Indique si B correspond à A à la position i
    for j in range(len_B):
        # Si le caractère de B est '_' alors il correspond à n'importe quel caractère d'A
        # Sinon, il doit correspondre exactement
        if B[j] != '_' and B[j] != A[i+j]:
            match = False
            break
    # Si on a trouvé une correspondance, on affiche "Yes" et on termine
    if match:
        print("Yes")
        break
else:
    # Si aucune correspondance n'a été trouvée, on affiche "No"
    print("No")