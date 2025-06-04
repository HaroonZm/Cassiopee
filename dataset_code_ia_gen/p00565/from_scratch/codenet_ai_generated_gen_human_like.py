N = int(input())
A = list(map(int, input().split()))

for dice_faces in range(1, N + 2):
    pos = 0
    visited = [False] * (N + 2)
    while pos < N + 1:
        pos += dice_faces
        if pos <= N and A[pos - 1] == 1:
            break
    else:
        print(dice_faces)
        break