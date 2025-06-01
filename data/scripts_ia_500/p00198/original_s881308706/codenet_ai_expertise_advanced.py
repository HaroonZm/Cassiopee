r = [
    [0,1,2,3,4,5,6], [0,1,3,5,2,4,6], [0,1,4,2,5,3,6], [0,1,5,4,3,2,6],
    [0,2,6,3,4,1,5], [0,2,3,1,6,4,5], [0,2,1,4,3,6,5], [0,2,4,6,1,3,5],
    [0,3,1,2,5,6,4], [0,3,2,6,1,5,4], [0,3,5,1,6,2,4], [0,3,6,5,2,1,4],
    [0,4,1,5,2,6,3], [0,4,2,1,6,5,3], [0,4,5,6,1,2,3], [0,4,6,2,5,1,3],
    [0,5,1,3,4,6,2], [0,5,3,6,1,4,2], [0,5,4,1,6,3,2], [0,5,6,4,3,1,2],
    [0,6,2,4,3,5,1], [0,6,3,2,5,4,1], [0,6,5,3,4,2,1], [0,6,4,5,2,3,1],
]

def are_equivalent(cube1, cube2):
    for perm in r:
        if all(cube1[perm[i]] == cube2[i] for i in range(1,7)):
            return True
    return False

from sys import stdin, stdout

input_iter = iter(stdin.read().splitlines())

while True:
    n = int(next(input_iter))
    if n == 0:
        break
    cubes = [ ('', *next(input_iter).split()) for _ in range(n) ]
    flagged = [False]*n
    for i in range(n):
        if flagged[i]:
            continue
        for j in range(i+1, n):
            if not flagged[j] and are_equivalent(cubes[i], cubes[j]):
                flagged[j] = True
    stdout.write(f"{sum(flagged)}\n")