N = int(input())
faces = []
for _ in range(N):
    p = list(map(int, input().split()))
    p.sort()
    faces.append(tuple(p))

unique_faces = set()
duplicates = 0
for face in faces:
    if face in unique_faces:
        duplicates += 1
    else:
        unique_faces.add(face)

print(duplicates)