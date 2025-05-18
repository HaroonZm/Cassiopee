def resolve():
    import sys
    from collections import deque
    input = sys.stdin.readline
    input()
    A = [int(i) for i in input().split()]
    input()
    B = [int(i) for i in input().split()]

    A = deque(A)
    B = deque(B)
    while len(A) > 0 and len(B) > 0:
        a = A.popleft()
        b = B.popleft()
        if a == b:
            continue
        elif a < b:
            print(1)
            return
        else:
            print(0)
            return
    if len(B) > 0:
        print(1)
    else:
        print(0)

resolve()