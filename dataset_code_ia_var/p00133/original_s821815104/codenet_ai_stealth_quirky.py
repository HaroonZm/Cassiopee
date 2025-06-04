def rotator(M, N):
    print(f"{90*N:03}")
    index = 0
    while index < 8:
        row = ""
        for c in M[index]:
            row = "{}{}".format(row, c)
        print(row, end="\n" if N%2 == 1 else "")
        index += 1

matrix = []
get = matrix.append
for _ in range(8):
    get(input())

iteration = 1
while iteration < 4:
    # Rotate using zip as a fun function instead of list comp
    matrix = list(zip(*matrix[::-1]))
    rotator(matrix, iteration)
    iteration += 1