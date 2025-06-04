while True:
    red = input()
    if red == '-':
        break
    green = input()
    down = input()

    # red, green, down are strings of unique characters
    # red packages come from top (vertical belt)
    # green packages come from left (horizontal belt)
    # down is the sequence of packages that reached the bottom belt after mixing

    # We need to reconstruct the sequence of packages that reached the right (right belt)

    # The mixing process is an interleaving of red and green packages:
    # Number of push_down = len(red)
    # Number of push_right = len(green) + 1
    # The first and last push are push_right
    # down represents the packages that reached bottom in order

    # Using down (bottom belt sequence), and red, green sequences,
    # reconstruct the right (right belt) output sequence

    # Approach:
    # Since the mixed sequence is an interleaving of red and green,
    # and down contains the packages that "fell" out of vertical belt (red),
    # we can simulate the interleaving and find the packages that fall out on the right belt (green's packages order).

    red_index = 0
    green_index = 0
    down_index = 0
    right = ''

    # The total output length is len(red)+len(green)
    # down contains len(red) packages

    # The mixed sequence is len(red)+len(green)

    # we simulate selecting from red or green:
    # if down[down_index] == red[red_index], it means a push_down happened (vertical belt package emitted)
    # else the emitted package must be from green (right belt), so we output it to right

    # Note: down and right are outputs, red and green are inputs

    while len(right) < len(green):
        # if next down package matches next red package, then it's a push_down
        if down_index < len(down) and red_index < len(red) and down[down_index] == red[red_index]:
            red_index += 1
            down_index += 1
        else:
            # this must be a push_right output package from green
            right += green[green_index]
            green_index += 1

    print(right)