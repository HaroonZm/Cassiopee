while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # ladder top floors pre-processing
    # For each ladder cell, find the top floor of ladder it belongs to
    def ladder_top(build):
        top = [0]*n
        i = 0
        while i < n:
            if build[i] == 1:
                j = i
                while j+1 < n and build[j+1] == 1:
                    j += 1
                for k in range(i, j+1):
                    top[k] = j
                i = j+1
            else:
                top[i] = i
                i += 1
        return top

    a_top = ladder_top(a)
    b_top = ladder_top(b)

    from collections import deque

    # State: (building(0 or 1), floor index 0-based)
    # Floors are 0-based internally for programming convenience
    # Start from floor 0 on either building
    visited = [[False]*n for _ in range(2)]

    queue = deque()
    # can start at floor 0 on building 0 and building 1
    # after being on floor 0, we can do jumps
    queue.append((0,0,0)) # building, floor, jumps
    queue.append((1,0,0))
    visited[0][0] = True
    visited[1][0] = True

    ans = "NA"

    while queue:
        bld,floor,jumps = queue.popleft()
        # if reached top floor, answer is jumps
        if floor == n-1:
            ans = jumps
            break
        # jump to the opposite building
        next_bld = 1 - bld

        # candidate floors: same floor, +1 floor, +2 floors
        for df in [0,1,2]:
            nf = floor + df
            if nf >= n:
                continue
            # after jump, adjust floor according to wall type
            if next_bld == 0:
                wall = a[nf]
                top_floor = a_top[nf]
            else:
                wall = b[nf]
                top_floor = b_top[nf]

            # process according to wall type
            if wall == 0:
                new_floor = nf
            elif wall == 1:
                new_floor = top_floor
            else: # wall == 2 slide
                # slide down to ladder top or normal floor
                # if ladder on that floor, slide down to top
                # otherwise, stay on nf
                if next_bld == 0:
                    new_floor = a_top[nf]
                else:
                    new_floor = b_top[nf]

            if not visited[next_bld][new_floor]:
                visited[next_bld][new_floor] = True
                queue.append((next_bld,new_floor,jumps+1))

    print(ans)