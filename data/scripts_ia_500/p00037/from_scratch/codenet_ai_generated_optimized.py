def main():
    h = [input() for _ in range(5)]
    v = [input() for _ in range(4)]

    W, H = 4, 5
    # create wall arrays: horizontal and vertical
    # h[i][j]: horizontal wall between (j,i) and (j+1,i)
    # v[i][j]: vertical wall between (j,i) and (j,i+1)

    # Directions: 0=up,1=right,2=down,3=left
    # dx,dy per direction
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    # helper to check wall to the right of (x,y) when facing direction d
    def has_wall_right(x,y,d):
        # right direction
        rd = (d+1)%4
        nx, ny = x+dx[rd], y+dy[rd]

        if rd == 0:
            # up: horizontal wall above y
            if ny < 0 or nx >= W:
                return True
            return h[ny][nx] == '1'
        elif rd == 1:
            # right: vertical wall to right of x
            if nx >= W or ny >= H:
                return True
            return v[ny][nx] == '1'
        elif rd == 2:
            # down: horizontal wall below y+1
            if y+1 >= H or nx >= W:
                return True
            return h[y+1][nx] == '1'
        else:
            # left: vertical wall to left of x
            if x-1 < 0 or ny >= H:
                return True
            return v[ny][x-1] == '1'

    def can_move(x,y,d):
        nx, ny = x+dx[d], y+dy[d]
        if nx < 0 or nx >= W or ny < 0 or ny >= H:
            return False
        if d == 0:
            return h[y][x] == '0'
        elif d == 1:
            return v[y][x] == '0'
        elif d == 2:
            return h[y+1][x] == '0'
        else:
            return v[y][x-1] == '0'

    # Start point A is (0,0), wall at top horizontal at h[0][0] must be 1 per problem
    x, y = 0, 0
    d = 1  # facing right
    route = []

    start = (x,y,d)
    while True:
        # try turn right
        if not has_wall_right(x,y,d):
            # turn right
            d = (d + 1) %4
            # move forward if possible
            nx, ny = x+dx[d], y+dy[d]
            route.append('RDLU'[d])
            x,y = nx,ny
        else:
            # if wall right, try forward
            nx, ny = x+dx[d], y+dy[d]
            if 0 <= nx < W and 0 <= ny < H:
                # check wall in front
                front_blocked = False
                if d == 0:
                    if h[y][x] == '1':
                        front_blocked = True
                elif d == 1:
                    if v[y][x] == '1':
                        front_blocked = True
                elif d == 2:
                    if h[y+1][x] == '1':
                        front_blocked = True
                else:
                    if v[y][x-1] == '1':
                        front_blocked = True
                if not front_blocked:
                    route.append('RDLU'[d])
                    x,y = nx,ny
                else:
                    # turn left
                    d = (d -1) % 4
            else:
                # turn left
                d = (d -1) % 4

        if (x,y,d) == start:
            break

    print(''.join(route))

if __name__ == "__main__":
    main()