import sys

# Mapping of directions to their column positions (x-coordinates) on the dance platform
# Directions (1-9 excluding 5), arranged as a numpad, with columns 1 to 3
# 7 8 9
# 4 5 6
# 1 2 3
# The pressed panels correspond to directions with coordinates:
# x is column from left (1,2,3)
# y is row from bottom (1,2,3)
# We'll only use x coordinate for foot placement constraints
direction_to_x = {
    1: 1, 2: 2, 3: 3,
    4: 1,       6: 3,
    7: 1, 8: 2, 9: 3
}

# Reads all datasets until '#'
def main():
    for line in sys.stdin:
        steps = line.strip()
        if steps == '#':
            break
        # Convert steps to list of integers
        seq = list(map(int, steps))

        # Dynamic programming approach:
        # We want to assign each step either to left (L) or right (R) foot
        # Constraint 1: At start, feet can be anywhere.
        # Constraint 2: At any time:
        #   left foot can't be on a panel whose x > right foot's panel x.
        #   right foot can't be on a panel whose x < left foot's panel x.
        # So left_foot_x <= right_foot_x must always hold.
        # Constraint 3: The minimum number of violations to natural style under the above conditions.
        # Natural style violation: when two consecutive steps are done by the same foot.
        #
        # State representation:
        # dp[i][l][r][f] = minimum number of violations up to step i
        # where left foot is on panel with x=l,
        # right foot on panel with x=r,
        # and last foot used is f (0=left, 1=right)
        #
        # However, this is too large (3*3 sides * 2 foot states * up to 100000 steps)
        # Optimization:
        # We can record only the positions, not exact panels, since the problem only cares about relative positions
        #
        # But actually dp on positions (left foot panel, right foot panel, last foot used) for 100k steps is impossible.
        #
        # Observe:
        # - Each step can be pressed either by left or right.
        # - We must keep track of the positions of left foot and right foot: the panel indexes.
        # - The positions can be any of the 8 directions.
        #
        # To limit complexity:
        # State: at step i,
        # For each possible last used foot (0=left,1=right),
        # For each possible position of left foot and right foot, store minimal violation count.
        #
        # Number of directions = 8 (1-9 except 5)
        # So up to 8*8*2=128 states per step.
        #
        # It's feasible if we use map/dictionary with pruning for each step.
        #
        # Implementation outline:
        # For each step in sequence:
        #   For each dp state from previous step:
        #       Try pressing current arrow with left foot and right foot if feasible.
        #       Update dp for next step.
        #
        # Initially, we have no previous positions or feet used.
        # So for first step, place left or right foot on current arrow with 0 violation.
        #
        # At each dp update:
        # Check feasibility constraints:
        #   left_foot_x <= right_foot_x (using direction_to_x)
        #
        # Count Violation:
        # If same foot as last step -> violation +1 else 0
        #
        # At end, minimal among all states is answer.

        dirs = [1,2,3,4,6,7,8,9]

        # For quick index mapping, create a list sorted of directions for indexing
        dir_list = dirs
        dir_index = {d:i for i, d in enumerate(dir_list)}

        # dp: dictionary with key = (left_dir_idx, right_dir_idx, last_foot)
        # value = minimal violation count so far
        # last_foot: 0=left,1=right,-1 no previous step
        dp = {}

        # Initialization: for first step, put left or right foot on the arrow, other foot anywhere (no constrain at start)
        # At start, we can put other foot anywhere, but initially unknown, so we try all possible positions for the other foot
        first_dir = seq[0]
        first_idx = dir_index[first_dir]

        # For the other foot, try all possible directions
        # violation=0 because first step never counts as violation
        for left_dir in dir_list:
            ld = dir_index[left_dir]
            for right_dir in dir_list:
                rd = dir_index[right_dir]
                # Both feet can be anywhere at start, no violation counted
                if first_dir == left_dir:
                    # Step pressed by left foot
                    if direction_to_x[left_dir] <= direction_to_x[right_dir]:
                        dp[(ld, rd, 0)] = 0
                if first_dir == right_dir:
                    # Step pressed by right foot
                    if direction_to_x[left_dir] <= direction_to_x[right_dir]:
                        # If left and right foot on same panel (which means same direction) is allowed (foot can overlap)
                        dp[(ld, rd, 1)] = 0

        # Process subsequent steps
        for step_i in range(1, len(seq)):
            curr_dir = seq[step_i]
            curr_idx = dir_index[curr_dir]
            next_dp = {}

            for (l_idx, r_idx, last_foot), violation_count in dp.items():
                l_dir = dir_list[l_idx]
                r_dir = dir_list[r_idx]

                # Try pressing current arrow with left foot
                # New left foot position = curr_dir, right foot position unchanged = r_dir
                if direction_to_x[curr_dir] <= direction_to_x[r_dir]:
                    new_violation = violation_count + (1 if last_foot == 0 else 0)
                    key = (curr_idx, r_idx, 0)
                    if key not in next_dp or next_dp[key] > new_violation:
                        next_dp[key] = new_violation

                # Try pressing current arrow with right foot
                # New right foot position = curr_dir, left foot position unchanged = l_dir
                if direction_to_x[l_dir] <= direction_to_x[curr_dir]:
                    new_violation = violation_count + (1 if last_foot == 1 else 0)
                    key = (l_idx, curr_idx, 1)
                    if key not in next_dp or next_dp[key] > new_violation:
                        next_dp[key] = new_violation

            dp = next_dp

        # At end, minimal violation count among all states is answer
        answer = min(dp.values()) if dp else 0
        print(answer)

if __name__ == "__main__":
    main()