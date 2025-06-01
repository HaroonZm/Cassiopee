import sys
input = sys.stdin.readline

C, N = map(int, input().split())
image = [list(map(int, list(input().rstrip()))) for _ in range(N)]

def is_symmetric(img):
    # Check vertical symmetry
    for r in range(N):
        for c in range(N // 2):
            if img[r][c] != img[r][N - 1 - c]:
                return False
    # Check horizontal symmetry
    for c in range(N):
        for r in range(N // 2):
            if img[r][c] != img[N - 1 - r][c]:
                return False
    return True

count = 0
if is_symmetric(image):
    count += 1

for _ in range(C - 1):
    D = int(input())
    for __ in range(D):
        r, c = map(int, input().split())
        r -= 1
        c -= 1
        image[r][c] = 1 - image[r][c]
    if is_symmetric(image):
        count += 1

print(count)