def parse_board(lines):
    return [list(line) for line in lines]

def board_has_hole_in_positions(board, positions):
    for r, c in positions:
        if board[r][c] == '*':
            return True
    return False

def can_pass(front, back):
    # positions to check: the bottom row and the two adjacent rows just above it in the middle columns
    # The problem states: at least one hole on lower three squares on front and back
    # but "lower three squares" on front and back means the bottom row (row=2) on each face
    # The puzzle says: "at least one hole on *at least one* of front or back lower three squares"
    # So if either front or back has hole in positions (2,0),(2,1),(2,2), it's OK
    positions = [(2,0),(2,1),(2,2)]
    return board_has_hole_in_positions(front, positions) or board_has_hole_in_positions(back, positions)

def rotate_cube(pos):
    # pos: tuple representing the current orientation of the dice:
    # We encode orientation by (front, right, top)
    # from these three faces we can deduce the others
    # faces: 0:front,1:right,2:back,3:left,4:top,5:bottom
    front, right, top = pos
    # The dice numbers are labels, we just track face indices.
    # But in input front=0,right=1,back=2,left=3,top=4,bottom=5
    # Using the standard dice rotation mapping:
    # Define dice faces
    # We'll rotate cube in four directions:
    # rotate forward: top->front, front->bottom, bottom->back, back->top
    def rotate_forward():
        return (5 - top), right, front
    # rotate backward: top->back, back->bottom, bottom->front, front->top
    def rotate_backward():
        return top, right, 5 - front
    # rotate right: front->left, left->back, back->right, right->front
    def rotate_right():
        return right, 5 - front, top
    # rotate left: front->right, right->back, back->left, left->front
    def rotate_left():
        return 5 - right, front, top

    return rotate_forward, rotate_backward, rotate_right, rotate_left

def get_all_orientations():
    # Each orientation of the dice can be uniquely defined by front, right, top face indices
    # But due to the fixed dice, there are 24 orientations maximum
    # We'll generate all by BFS starting from (0,1,4)
    from collections import deque
    start = (0,1,4)
    seen = set()
    q = deque()
    q.append(start)
    moves = rotate_cube(start)
    orientations = []
    while q:
        ori = q.popleft()
        if ori in seen:
            continue
        seen.add(ori)
        orientations.append(ori)
        rotate_forward, rotate_backward, rotate_right, rotate_left = rotate_cube(ori)
        for rot in (rotate_forward, rotate_backward, rotate_right, rotate_left):
            new_ori = rot()
            if new_ori not in seen:
                q.append(new_ori)
    return orientations

def rotate_board_90(board):
    # rotate board 90 deg clockwise
    n = len(board)
    new_board = [['']*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            new_board[c][n-1-r] = board[r][c]
    return new_board

def rotate_face(board, count):
    # rotate face count times 90 degrees clockwise
    for _ in range(count):
        board = rotate_board_90(board)
    return board

def orientation_to_map(ori):
    # return dict face_index-> orientation of that face in input boards
    # we track the faces orientation:
    # because when dice is rotated, the face rotation differs
    # We chose as fixed: faces in input: front, right, back, left, top, bottom
    # indices 0..5

    # dice orientation (front,right,top) gives permutation of faces with some rotation.
    # We use a known method:
    # We will build 6 faces of the oriented dice from the input faces:

    # face indices:
    # 0: front
    # 1: right
    # 2: back
    # 3: left
    # 4: top
    # 5: bottom

    # dice orientation is (front, right, top), each from 0..5

    front, right, top = ori
    bottom = 5 - top
    left = 5 - right
    back = 5 - front

    # The "face_info" is dict[new_face_index] = (input_face_index, rotation)
    # rotation is number of times clockwise rotated the input face to get oriented face

    # Determine rotation for each face so that all faces are correctly oriented relative to front, right, top faces.

    # We can consider coordinates and use cross product:
    # but instead we do hardcoded lookups based on cube orientation:
    # We'll define relative orientations of dice faces.

    # Define vector for each face in the starting orientation:
    # We'll represent faces as vectors:
    # front = (0, 1, 0)
    # back = (0, -1, 0)
    # left = (-1, 0, 0)
    # right = (1, 0, 0)
    # top = (0, 0, 1)
    # bottom = (0, 0, -1)

    # We want to find rotation of each input face to get correct "up" orientation from the current orientation

    # To do this accurately we need to track the orientation of each face.

    # We'll store for each face its forward vector and up vector

    # Base orientation face to forward, up:

    base_forward = {
        0: (0, 1, 0),  # front
        1: (1, 0, 0),  # right
        2: (0, -1, 0), # back
        3: (-1,0, 0),  # left
        4: (0, 0, 1),  # top
        5: (0, 0, -1)  # bottom
    }
    base_up = {
        0: (0, 0, 1),
        1: (0, 0, 1),
        2: (0, 0, 1),
        3: (0, 0, 1),
        4: (0, 1, 0),
        5: (0, -1, 0)
    }

    # We know front, right, top are facing directions, actual vectors.

    # We must find the rotation from input face orientation to oriented dice face orientation.

    # Let's create a map face->(forward,up)
    # The oriented dice faces' forward vector and up vector must be compatible with orientation front,right,top.

    # The oriented dice face vectors:

    # front = front vector
    # right = right vector
    # top = top vector
    # back = -front
    # left = -right
    # bottom = -top

    oriented_forward = {
        0: base_forward[front],
        1: base_forward[right],
        2: tuple(-x for x in base_forward[front]),
        3: tuple(-x for x in base_forward[right]),
        4: base_forward[top],
        5: tuple(-x for x in base_forward[top])
    }
    oriented_up = {
        0: base_up[front],
        1: base_up[right],
        2: base_up[back],
        3: base_up[left],
        4: base_up[top],
        5: base_up[bottom]
    }
    # We use the base_up vectors for back,left,bottom correctly:
    # Let's adjust base_up for back,left,bottom:
    # back = 2
    # left = 3
    # bottom = 5

    # Assign ups based on base_up of input face opposite to corresponding oriented face:
    base_up[2] = (0,0,1)
    base_up[3] = (0,0,1)
    base_up[5] = (0,-1,0)

    oriented_up[2] = base_up[2]
    oriented_up[3] = base_up[3]
    oriented_up[5] = base_up[5]

    # Now compute rotation (0,1,2,3) for each face to get input face map to oriented face.
    # The rotation is number of 90 degree clockwise rotations on the input face to orient it.

    # We do this by comparing directions.
    # The front of the input face is vector (0,1,0) and up is (0,0,1).
    # The rotations are:
    # 0: forward=(0,1,0), up=(0,0,1)
    # 1: rotate 90: forward=(1,0,0), up=(0,0,1)
    # 2: rotate 180: forward=(0,-1,0), up=(0,0,1)
    # 3: rotate 270: forward=(-1,0,0), up=(0,0,1)
    # We can determine rotation by seeing where the target forward matches

    # Since the base orientation input face is (0,1,0) forward, (0,0,1) up, rotate clockwise each step means forward vector cycles through above.

    input_forwards = [(0,1,0),(1,0,0),(0,-1,0),(-1,0,0)]
    input_ups =    [(0,0,1),(0,0,1),(0,0,1),(0,0,1)]

    # For top and bottom, the input orientation is different,
    # top input has forward=(0,0,1), up=(0,1,0)
    # bottom input has forward=(0,0,-1), up=(0,-1,0)

    rotation_map = {}

    for face in range(6):
        input_face = face  # face index of input face for this location
        # input face forward/up
        if input_face in (4,5):
            # top or bottom
            # We define their 4 rotations as:
            # 0: forward=(0,0,1) or (0,0,-1), up=(0,1,0) or (0,-1,0)
            # Rotations here change forward/up differently (rotating around forward)
            # Instead we can avoid complexity by hardcoding rotations

            # Let's take all 4 rotations' up vectors for top and bottom
            # Rotations on top/bottom faces correspond to rotation around forward axis
            # So forward stays same, up changes in circle: (0,1,0)->(1,0,0)->(0,-1,0)->(-1,0,0)

            input_forward = base_forward[input_face]
            input_up = base_up[input_face]
            candidates = []
            # simulate 4 rotations clockwise on the face (around forward)
            ux, uy, uz = input_up
            # For each rotation, the up vector rotates around forward axis by 90 deg
            # We can hardcode 4 up vectors for top/bottom face rotations
            # The possible up vectors are (0,1,0),(1,0,0),(0,-1,0),(-1,0,0)

            ups = [(0,1,0),(1,0,0),(0,-1,0),(-1,0,0)]
            rotations = []
            for rot in range(4):
                # Up for rotation "rot" is ups[rot]
                rotations.append((input_forward, ups[rot]))

            oriented_fwd = oriented_forward[face]
            oriented_upv = oriented_up[face]

            # find rotation where forward matches and up matches oriented_up
            rot_found = None
            for rot, (fwd, upv) in enumerate(rotations):
                if fwd == oriented_fwd and upv == oriented_upv:
                    rot_found = rot
                    break
            if rot_found is None:
                rot_found = 0
        else:
            # for front,right,back,left faces
            # input forward = (0,1,0)
            # input up=(0,0,1)

            oriented_fwd = oriented_forward[face]
            oriented_upv = oriented_up[face]

            rot_found = None
            for rot, fwd in enumerate(input_forwards):
                if fwd == oriented_fwd and input_ups[rot] == oriented_upv:
                    rot_found = rot
                    break
            if rot_found is None:
                # maybe rotated input is flipped? For simplicity assume 0
                rot_found = 0

        rotation_map[face] = rot_found

    # We return a map of face_index: (input_face_index, rotation_count)
    # input_face_index is the input face that corresponds to oriented face: mapping is:
    input_face_map = {
        0: front,
        1: right,
        2: back,
        3: left,
        4: top,
        5: bottom
    }

    face_map = {}
    for face in range(6):
        face_map[face] = (input_face_map[face], rotation_map[face])
    return face_map

def apply_orientation(boards, face_map):
    # boards: list of 6 boards - input faces
    # face_map: dict face->(input_face, rotations)

    res = [None]*6
    for face in range(6):
        input_face, rots = face_map[face]
        b = [row[:] for row in boards[input_face]]
        b = rotate_face(b, rots)
        res[face] = b
    return res

def solve_dataset(boards):
    # boards is a list of 6 faces in input orientation (front,right,back,left,top,bottom)

    # We want minimal rotations to get dice orientation allowing to pass

    # We start from orientation (0,1,4)

    from collections import deque

    start_ori = (0,1,4)
    orientations = get_all_orientations()
    dist = {}
    q = deque()
    dist[start_ori] = 0
    q.append(start_ori)

    while q:
        ori = q.popleft()
        d = dist[ori]

        face_map = orientation_to_map(ori)
        oriented_boards = apply_orientation(boards, face_map)
        front = oriented_boards[0]
        back = oriented_boards[2]

        if can_pass(front, back):
            return d

        rotate_forward, rotate_backward, rotate_right, rotate_left = rotate_cube(ori)
        for new_ori in [rotate_forward(), rotate_backward(), rotate_right(), rotate_left()]:
            if new_ori not in dist:
                dist[new_ori] = d+1
                q.append(new_ori)
    return -1  # should not happen per problem statement

def main():
    import sys
    lines = []
    for line in sys.stdin:
        line = line.rstrip('\n')
        if line == '#':
            break
        lines.append(line)
    idx = 0
    n = len(lines)
    while idx < n:
        if lines[idx] == '':
            idx += 1
            continue
        if idx+18 > n:
            break
        boards_raw = lines[idx:idx+18]
        idx += 18
        boards = []
        # six faces, each 3 lines
        for i in range(6):
            board = parse_board(boards_raw[i*3:(i+1)*3])
            boards.append(board)
        # skip blank line
        if idx<n and lines[idx]=='':
            idx+=1
        ans = solve_dataset(boards)
        print(ans)

if __name__=="__main__":
    main()