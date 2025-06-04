from sys import stdin

# Mapping of opposite faces on a die
opposite = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}

# The directions the die can roll, associated with face on which it rolls over
# For each face on bottom, which face will be on bottom after rolling in direction of 4,5,6
# But since faces can be at top/front/etc, we need to be able to handle arbitrary orientations

# We represent die orientation by top, front, right, left, back, bottom faces.
# We only know top and front at start; from these we can find others.

# Helper to get right face given top and front
def get_right(top, front):
    # Faces arranged so that right is the face that makes top, front and right a right hand coordinate system
    # Given opposites: 1-6,2-5,3-4
    # Faces: top, bottom, front, back, left, right
    # Directions: 
    # For a standard die:
    #   top-opposite=bottom
    #   front-opposite=back
    #   left-opposite=right
    # We can determine right: right is the face that is different from top, front and doesn't share opposite with front or top and is consistent
    faces = {1,2,3,4,5,6}
    bottom = opposite[top]
    back = opposite[front]
    # Candidates for right: faces not top,bottom,front,back
    candidates = faces - {top, bottom, front, back}
    # Among candidates one is right, the other is left
    # We'll pick right as the one where left is opposite(right)
    # But left-opposite=right, so the pair left/right is pair from candidates
    # Just pick min as right, max as left
    right = min(candidates)
    left = max(candidates)
    return right, left, back, bottom

# Represent a die orientation as a tuple of (top, front)
# We can find other faces from this by function get_all_faces

def get_all_faces(top, front):
    right, left, back, bottom = get_right(top, front)
    return {'top':top, 'front':front, 'right':right, 'left':left, 'back':back, 'bottom':bottom}

# Roll the die 90 degrees towards a given direction face: 4,5,6 (direction is the face the die rolls towards)
# Directions correspond to faces on side of die that the die can roll on.
# Rolling means the die rotates 90 degrees so that face in that direction becomes bottom,
# top changes accordingly, front changes accordingly.

# We need to define how the orientation changes after rolling towards face 4,5 or 6.

# Let's consider that rolling towards face X means the die rolls over the edge adjacent to the face X.

# We can implement roll functions relative to the current orientation.

# We will build a function roll(orientation, direction) -> new orientation

def roll(orient, direction):
    # Input: orient: dict with keys top, front, right, left, back, bottom (faces)
    # direction: face number (4,5,6)
    top = orient['top']
    front = orient['front']
    right = orient['right']
    left = orient['left']
    back = orient['back']
    bottom = orient['bottom']
    # Rolling towards face 4 means the die rolls in the direction where face 4 lies.
    # The die can only roll to faces 4,5,6 that are currently on sides.
    # We find which face direction means:
    # The die rolls so that that face goes from side to bottom.
    # Face on bottom moves to opposite side.
    # Faces change similarly.

    # We find which side the direction face is (front, right, left, back).
    # Then we change orientation accordingly.

    if direction == orient['front']:
        # roll forward: top->back, front->top, bottom->front, back->bottom, right and left stay
        return {
            'top': back,
            'front': top,
            'right': right,
            'left': left,
            'back': bottom,
            'bottom': front
        }
    elif direction == orient['back']:
        # roll backward: top->front, back->top, bottom->back, front->bottom, right and left stay
        return {
            'top': front,
            'front': bottom,
            'right': right,
            'left': left,
            'back': top,
            'bottom': back
        }
    elif direction == orient['right']:
        # roll right: top->left, right->top, bottom->right, left->bottom, front and back stay
        return {
            'top': left,
            'front': front,
            'right': top,
            'left': bottom,
            'back': back,
            'bottom': right
        }
    elif direction == orient['left']:
        # roll left: top->right, left->top, bottom->left, right->bottom, front and back stay
        return {
            'top': right,
            'front': front,
            'right': bottom,
            'left': top,
            'back': back,
            'bottom': left
        }
    else:
        # The face to roll towards must be among 4,5,6 and on sides
        # But 4/5/6 must be on one of the four sides, or bottom or top.
        # Rolling towards bottom or top is invalid.
        # We'll never roll towards top or bottom.
        # So if direction isn't on sides, do nothing
        return orient

# Determine which directions (among faces 4,5,6) the die can roll to from current orientation

def can_roll_dirs(orient):
    # Can only roll towards faces 4,5,6 that are on sides: front, right, left, back
    res = []
    for face in [orient['front'], orient['right'], orient['left'], orient['back']]:
        if face in {4,5,6}:
            res.append(face)
    return res

# Simulate dropping a die on the stack at position x:
# The plane is a line of stacks, each stack is a list of dice orientations from bottom to top
# We drop dice at position 0 (the single fixed position). Stacks indexed by horizontal coordinate.
# But dice can roll to neighbor stacks.

# We store stacks in a dict x=>list of orientations (bottom to top)

# For vertical height, the index of dice in stack is their height.

# When a die falls, it falls down until the bottom face touches the floor or a die.

# Inputs:
# stacks: dict[int, list of orientations]
# new_die: orientation of dropped die
# Returns new stacks after full rolling and dropping simulation

# To determine if die can roll to neighbor stack, it must 'fall down' after rolling:
# That means the neighbor stack height is less than the current height of the die

# Also, the die rolls only if after rolling and falling, it falls down (i.e. neighbor stack is lower than current stack height)

# We'll proceed as follows:
# Place the die initially at x=0, height = current stack height at x=0
# Then simulate rolling repeatedly until no moves possible
# Each roll is 90 degrees to one direction face 4,5,6 among sides
# Check if neighbor stack at x+dx has height less than current height, for the direction
# The direction is face on side, so moving left or right:
# We need mapping face to dx: which corresponds to horizontal movement

# Since the plane is a line from left to right, we must know for each side face if it corresponds to left or right

# Let's define that rolling towards 'left' face moves x-1, 'right' face moves x+1, 'front' or 'back' moves no horizontal change => invalid to roll in that direction (since no plane).

# But problem states it's on a plane (2D), but dice are 3D... but problem statement seems to imply a 1D line for positions.

# Actually, problem says "dropping dice from fixed position", they may roll left or right according to properties.

# So horizontal positions track integer positions on a line.

# Movement:

# Rolling towards face 4 means going to position x-1

# Rolling towards face 5 means staying at x (forward or backward)

# Rolling towards face 6 means going to position x+1

# But problem states dice can roll only in directions of faces 4,5,6.

# But in example, dice can roll either left or right.

# We map directions to horizontal movement based on which face is at what relative side:

# We decide:

# face 4 => move left (-1)

# face 5 => stay (0)

# face 6 => move right (+1)

# Rolling direction is direction of the face to roll towards (4,5,6)

# So if the die's side face 4 is on left, rolling towards 4 means move x-1

# If die's side face 6 is on right, scrolling towards 6 means x+1

# If face 5 is front or back (no horizontal movement), we consider that no horizontal movement => invalid

# So since the problem aligns to a plane (line), only rolling to left or right stacks (x-1 or x+1) is allowed

# So only rolling towards 4 (left) and 6 (right) cause horizontal movement, rolling towards 5 (front or back) is no horizontal movement (no stack to fall off), so no roll.

# Actually problem states: "dice never roll in directions of faces 1,2,3 but only in directions of faces 4,5,6"

# And the die rolls of a 90 degree exactly.

# But the problem example shows rolls to the sides, so possibly face 4 is always left, face 5 is front, face 6 is right

# So:

# rolling towards face 4 (left) dx = -1

# rolling towards face 5 (front): dx = 0

# rolling towards face 6 (right): dx = +1

# For rolling towards face 5 (front), no horizontal movement, so no position change, so no falling to new stack

# So rolling towards 5 means no horizontal movement, we see what that implies

# For falling condition: die rolls only when it can fall down after rolling: the neighbor stack height after rolling must be less than current height

# For rolling towards 5 (dx=0), neighbor stack = current stack (x)

# The die can fall only if the neighbor stack height < current height

# Since it's the same stack, height is same or higher, so die can't fall (unless stack is shorter?), possible only if top die is removed?

# But from problem ex and logic, rolling forward (towards 5/face front) does not cause horizontal move, so no falling off.

# But problem examples show rolling only moves left or right.

# So we conclude that rolling towards face 5 (front) means no horizontal move, so no falling, so no roll.

# So dice roll only towards faces 4 and 6 that correspond to horizontal move.

# In problem, dice can roll only towards faces 4,5,6, but rolling only when can fall, rolling towards 5 is impossible since no falling.

# We'll proceed to allow rolling only towards faces 4 and 6.

# We'll check neighbor stacks at x-1 and x+1.

# Let's implement this.

def simulate_drop(stacks, die_orientation):
    # start position x=0
    x = 0
    # stack height at x
    h = len(stacks.get(x, []))
    # current orientation
    orient = die_orientation
    # We'll simulate rolling until no roll possible

    while True:
        # Find directions to roll: faces 4 or 6 on sides (left or right)
        # faces 5 do not cause horizontal move, so ignore
        directions = []
        for face in [orient['front'], orient['right'], orient['left'], orient['back']]:
            if face in {4,6}: 
                directions.append(face)
        if not directions:
            break
        # For each direction, check if rolling is possible:
        # Rolling possible only if after rolling and falling, die falls down:
        # That is, neighbor stack height less than current height

        # Check candidate rolls
        candidates = []
        for d in directions:
            # Calculate horizontal shift dx
            # Find which side face d is on
            # left or right
            if d == 4:
                dx = -1
            elif d == 6:
                dx = +1
            else:
                # face 5 or others ignored
                continue
            # Height at neighbor stack
            nh = len(stacks.get(x + dx, []))
            if nh < h:
                candidates.append((d, nh, dx))
        if not candidates:
            break
        # If multiple candidates, roll towards the face with the largest number
        candidates.sort(reverse=True, key=lambda x: x[0])
        d, nh, dx = candidates[0]

        # Roll die towards d
        orient = roll(orient, d)
        # Update position and height
        x = x + dx
        h = nh
        # After rolling, die falls down to height nh
        # Repeat until no roll possible

    # After rolling complete, place the die on the stack at x at height h
    if x not in stacks:
        stacks[x] = []
    stacks[x].append(orient)
    return stacks

# Get visible top faces of all stacks
# The visible face for a die on top is its top face
# On the stacking line, only the top dice visible (top face)

# We count how many times each face number (1..6) appears on top faces

def count_visible_faces(stacks):
    count = [0]*6
    for stack in stacks.values():
        if stack:
            top_orient = stack[-1]
            f = top_orient['top']
            count[f-1] += 1
    return count


# Parse input and simulate

def from_tf_to_orientation(t,f):
    # Given initial top t and front f, get full orientation
    # Check direction validity: front != top and front != opposite(top)
    # Should be, problem guarantees input valid
    return get_all_faces(t,f)

def main():
    lines = stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx>=len(lines):
            break
        nline = lines[idx].strip()
        idx+=1
        if nline == '0':
            break
        n = int(nline)
        stacks = dict()
        # For each die, get t,f
        for _ in range(n):
            t,f = map(int, lines[idx].split())
            idx+=1
            orient = from_tf_to_orientation(t,f)
            stacks = simulate_drop(stacks, orient)
        res = count_visible_faces(stacks)
        print(' '.join(map(str,res)))

main()