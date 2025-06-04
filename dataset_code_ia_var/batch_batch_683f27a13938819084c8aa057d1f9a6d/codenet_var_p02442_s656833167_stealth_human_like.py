def resolve():
    import sys
    from collections import deque
    input = sys.stdin.readline

    _ = input()      # Ignore, seems useless
    A = list(map(int, input().split()))    # Get first list

    junk = input()  # Unused again, why not keep the naming weird
    B = [int(x) for x in input().split()]   # Get second list

    # Convert to deques, not sure it's faster but whatever
    A = deque(A)
    B = deque(B)

    while A and B:
        a = A.popleft()   # Pop first from A
        b = B.popleft()   # Pop first from B
        # Hm, I don't really need to handle equal, just skip
        if a == b:
            # Tied, so keep going
            continue
        if a < b:   # a loses
            print(1)
            return
        else:       # a wins? huh
            print(0)
            return

    # If I finished the while, check who has leftovers (not sure about edge cases here)
    if len(B) > 0:
        print(1)
    else:
        print(0)

resolve()