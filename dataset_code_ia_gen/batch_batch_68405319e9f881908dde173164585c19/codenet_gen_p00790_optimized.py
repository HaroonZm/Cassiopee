def main():
    while True:
        n = int(input())
        if n == 0:
            break

        # Faces: top, bottom, north, south, west, east
        # Initial according to problem:
        # top=1, north=2, west=3
        # Opposite faces sum to 7:
        # bottom=6, south=5, east=4
        top, bottom, north, south, west, east = 1, 6, 2, 5, 3, 4

        for _ in range(n):
            cmd = input()
            if cmd == 'north':
                # Roll to north:
                # new top = south
                # new bottom = north
                # new north = top
                # new south = bottom
                top, bottom, north, south = south, north, top, bottom
            elif cmd == 'south':
                # Roll to south:
                # new top = north
                # new bottom = south
                # new north = bottom
                # new south = top
                top, bottom, north, south = north, south, bottom, top
            elif cmd == 'east':
                # Roll to east:
                # new top = west
                # new bottom = east
                # new west = bottom
                # new east = top
                top, bottom, west, east = west, east, bottom, top
            else:  # west
                # Roll to west:
                # new top = east
                # new bottom = west
                # new west = top
                # new east = bottom
                top, bottom, west, east = east, west, top, bottom

        print(top)


if __name__ == '__main__':
    main()