C, N = map(int, input().split())
pixels = []
for _ in range(N):
    line = input()
    pixels.append([int(ch) for ch in line])

def is_symmetric(image):
    # Check vertical symmetry
    for r in range(N):
        for c in range(N // 2):
            if image[r][c] != image[r][N - 1 - c]:
                return False
    # Check horizontal symmetry
    for r in range(N // 2):
        for c in range(N):
            if image[r][c] != image[N - 1 - r][c]:
                return False
    return True

count = 0
if is_symmetric(pixels):
    count += 1

for _ in range(C - 1):
    D = int(input())
    for __ in range(D):
        r, c = map(int, input().split())
        # flip pixel at (r-1, c-1)
        pixels[r-1][c-1] = 1 - pixels[r-1][c-1]
    if is_symmetric(pixels):
        count += 1

print(count)