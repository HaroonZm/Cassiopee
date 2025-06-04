N=int(input())
faces = set()
duplicates = 0
for _ in range(N):
    face = tuple(sorted(map(int, input().split())))
    if face in faces:
        duplicates += 1
    else:
        faces.add(face)
print(duplicates)