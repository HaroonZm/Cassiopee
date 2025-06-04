rectangles = []
for _ in range(6):
    h, w = map(int, input().split())
    if h > w:
        h, w = w, h
    rectangles.append((h, w))

rectangles.sort()

# Pour qu'un parallélépipède rectangle soit formé, les 6 rectangles doivent se grouper par 3 paires identiques
# Chaque paire représente une des faces, et il y a 3 dimensions.
# On vérifie donc les paires consécutives après tri.

if (rectangles[0] == rectangles[1] and
    rectangles[2] == rectangles[3] and
    rectangles[4] == rectangles[5]):
    # On extrait les dimensions uniques
    a = rectangles[0]
    b = rectangles[2]
    c = rectangles[4]

    # Pour que ce soit un parallélépipède rectangle, les trois paires doivent correspondre à 3 dimensions formant un rectangle
    # Cela signifie que les côtés doivent s'associer correctement.
    # Les faces doivent être (a,b), (b,c), (a,c) dans n'importe quel ordre.

    faces = [a, b, c]
    faces_sorted = [sorted(face) for face in faces]
    faces_sorted.sort()

    # Les combinaisons possibles de faces sont (l,w), (w,h), (l,h) où (l,w,h) sont les dimensions.

    # Récupérons les côtés distincts
    sides = []
    for f in faces_sorted:
        sides.extend(f)
    sides = list(set(sides))
    if len(sides) > 3:
        print("no")
    else:
        # Construisons les 3 faces possibles à partir des 3 dimensions
        sides.sort()
        expected_faces = [sorted([sides[0], sides[1]]), sorted([sides[1], sides[2]]), sorted([sides[0], sides[2]])]
        expected_faces.sort()
        if faces_sorted == expected_faces:
            print("yes")
        else:
            print("no")
else:
    print("no")