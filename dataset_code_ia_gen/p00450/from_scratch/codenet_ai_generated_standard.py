import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    stones = [int(input()) for _ in range(n)]
    stack = []  # (color, count)
    for i, c in enumerate(stones, 1):
        if i % 2 == 1:
            # odd i: just add new stone
            if stack and stack[-1][0] == c:
                stack[-1] = (c, stack[-1][1] + 1)
            else:
                stack.append((c, 1))
        else:
            if not stack:
                stack.append((c,1))
            else:
                right_color = stack[-1][0]
                if c == right_color:
                    # same color: just add
                    stack[-1] = (c, stack[-1][1] + 1)
                else:
                    # different: remove right-end consecutive stones
                    tail_count = stack[-1][1]
                    stack.pop()
                    # replace with c repeated tail_count times
                    if stack and stack[-1][0] == c:
                        stack[-1] = (c, stack[-1][1] + tail_count)
                    else:
                        stack.append((c, tail_count))
                    # then put c stone at right end
                    stack[-1] = (c, stack[-1][1] + 1)

    # count white stones (color 0)
    ans = sum(count for color, count in stack if color == 0)
    print(ans)