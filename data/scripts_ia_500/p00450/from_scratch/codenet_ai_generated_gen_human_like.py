while True:
    n = int(input())
    if n == 0:
        break
    stones = []
    for i in range(n):
        c = int(input())
        if i % 2 == 0:  # i+1 is odd (1-based)
            stones.append([c, 1])
        else:  # i+1 is even
            right_color = stones[-1][0]
            if c == right_color:
                stones.append([c, 1])
            else:
                right_group_color = stones[-1][0]
                right_group_count = stones[-1][1]
                # remove right group's same color stones
                stones.pop()
                # add group with current color and same count as removed group
                stones.append([c, right_group_count])
                # then add one stone of current color at right end
                stones.append([c, 1])
    # count white stones (color 0)
    white_count = sum(count for color, count in stones if color == 0)
    print(white_count)