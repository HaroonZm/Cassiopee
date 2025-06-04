import sys

def wait_for_input():
    input()

def read_input():
    return sys.stdin

def split_line(line):
    return line.split()

def convert_to_floats(strs):
    return list(map(float, strs))

def extract_circle_data(data):
    xa = data[0]
    ya = data[1]
    ra = data[2]
    xb = data[3]
    yb = data[4]
    rb = data[5]
    return xa, ya, ra, xb, yb, rb

def distance(xa, ya, xb, yb):
    dx = xa - xb
    dy = ya - yb
    return (dx * dx + dy * dy) ** 0.5

def is_disjoint(dist, ra, rb):
    return dist > ra + rb

def is_b_inside_a(dist, ra, rb):
    return dist + rb < ra

def is_a_inside_b(dist, ra, rb):
    return dist + ra < rb

def process_circles(xa, ya, ra, xb, yb, rb):
    dist = distance(xa, ya, xb, yb)
    if is_disjoint(dist, ra, rb):
        return 0
    elif is_b_inside_a(dist, ra, rb):
        return 2
    elif is_a_inside_b(dist, ra, rb):
        return -2
    else:
        return 1

def main():
    wait_for_input()
    for s in read_input():
        strs = split_line(s)
        floats = convert_to_floats(strs)
        xa, ya, ra, xb, yb, rb = extract_circle_data(floats)
        result = process_circles(xa, ya, ra, xb, yb, rb)
        print(result)

if __name__ == "__main__":
    main()