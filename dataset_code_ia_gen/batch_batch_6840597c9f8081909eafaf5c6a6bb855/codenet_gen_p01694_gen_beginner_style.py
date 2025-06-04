while True:
    n = int(input())
    if n == 0:
        break
    moves = input().split()

    # 0 means foot on the floor, 1 means foot on the stepping platform
    left = 0
    right = 0
    count = 0
    # States:
    # 0: both feet on floor
    # 1: one foot on platform
    # 2: both feet on platform
    # We start at state 0
    for move in moves:
        if move == "lu":
            left = 1
        elif move == "ru":
            right = 1
        elif move == "ld":
            left = 0
        elif move == "rd":
            right = 0

        # Check if we made a correct step count:
        # If both feet on floor or both feet on platform now,
        # and previous state was different, count one step
        if left == right:
            count += 1
            left = 0 if left==0 else 1
            right = left  # sync both feet
    # the above counts too many times because we count on every state where feet match;
    # correct way: count only transitions from 0 to 2 or 2 to 0 of feet positions:
    # so let's track previous state and count only when current state differs and both feet match

while True:
    n = int(input())
    if n == 0:
        break
    moves = input().split()

    left = 0
    right = 0
    count = 0
    prev_state = 0  # 0 or 2

    for move in moves:
        if move == "lu":
            left = 1
        elif move == "ru":
            right = 1
        elif move == "ld":
            left = 0
        elif move == "rd":
            right = 0

        if left == right:  # both feet at same position, either floor or step
            curr_state = left * 2  # 0 if floor, 2 if step
            if curr_state != prev_state:
                count += 1
                prev_state = curr_state

    print(count)