def solve():
    import sys
    file_input = sys.stdin
    
    N, M, Q = map(int, file_input.readline().split())
    
    from collections import deque
    student = deque(range(N))
    exemption = [1] * N
    for a in map(int, file_input.readline().split()):
        if a % 2:
            student.rotate(a)
        else:
            student.rotate(-a)
        s = student.popleft()
        exemption[s] = 0
    
    question = map(int, file_input.readline().split())
    print(*map(lambda x: exemption[x], question), sep = '\n')

solve()