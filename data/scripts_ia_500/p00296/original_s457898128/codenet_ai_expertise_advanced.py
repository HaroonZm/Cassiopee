def solve():
    import sys
    from collections import deque
    input = sys.stdin.readline

    N, M, Q = map(int, input().split())
    rotations = map(int, input().split())
    questions = list(map(int, input().split()))

    students = deque(range(N))
    exemption = [1] * N

    for a in rotations:
        students.rotate(a if a % 2 else -a)
        exemption[students.popleft()] = 0

    print(*map(exemption.__getitem__, questions), sep='\n')

solve()