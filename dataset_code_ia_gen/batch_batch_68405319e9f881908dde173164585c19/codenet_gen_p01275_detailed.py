def min_rotations(k, initial, target):
    # Convert initial and target strings into lists of integers for easier manipulation
    init_nums = list(map(int, initial))
    target_nums = list(map(int, target))
    
    # We keep track of the current state of the dials
    current = init_nums[:]
    rotations = 0
    
    # We process dials from left to right
    # At each position, if the current dial does not match the target,
    # we will rotate a contiguous block of dials starting at this position
    # by the minimal needed amount (either left or right rotation)
    i = 0
    while i < k:
        if current[i] != target_nums[i]:
            # Determine difference in numbers mod 10 in both directions
            diff_right = (current[i] - target_nums[i]) % 10  # rotating right by diff_right steps
            diff_left = (target_nums[i] - current[i]) % 10   # rotating left by diff_left steps
            
            # choose minimal rotation count
            if diff_left <= diff_right:
                rotate_steps = diff_left
                direction = 'left'  # rotating left increases the number
            else:
                rotate_steps = diff_right
                direction = 'right'  # rotating right decreases the number
            
            # Find how far this rotation can extend to the right
            # All adjacent dials that require rotation by the same steps in the same direction
            j = i
            while j < k:
                # calculate the difference for dial j
                curr_val = current[j]
                targ_val = target_nums[j]
                
                d_right = (curr_val - targ_val) % 10
                d_left = (targ_val - curr_val) % 10
                
                if direction == 'left' and d_left == rotate_steps:
                    j += 1
                elif direction == 'right' and d_right == rotate_steps:
                    j += 1
                else:
                    break
            
            # Rotate the dials from i to j-1 in the chosen direction by rotate_steps
            for idx in range(i, j):
                if direction == 'left':
                    # rotating left by i digits means pointing to i-th right number
                    # So number increases by rotate_steps modulo 10
                    current[idx] = (current[idx] + rotate_steps) % 10
                else:
                    # rotating right by i digits means pointing to i-th left number
                    # So number decreases by rotate_steps modulo 10
                    current[idx] = (current[idx] - rotate_steps + 10) % 10
            
            rotations += 1
            i = j  # continue from dial j (first dial not rotated this time)
        else:
            i += 1
    
    return rotations

# Main program to read input and print results
while True:
    k = int(input())
    if k == 0:
        break
    initial, target = input().split()
    print(min_rotations(k, initial, target))