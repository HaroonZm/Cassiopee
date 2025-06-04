def read_dimensions():
    return list(map(int, input().split()))

def read_grid_row():
    return list(input())

def read_grid(h):
    grid = []
    for _ in range(h):
        grid.append(read_grid_row())
    return grid

def is_hash(cell):
    return cell == '#'

def count_hashes_in_row(row):
    count = 0
    for cell in row:
        if is_hash(cell):
            count += 1
    return count

def count_hashes(grid):
    total = 0
    for row in grid:
        total += count_hashes_in_row(row)
    return total

def required_hash_count(h, w):
    return (h + w) - 1

def check_possible(cnt, required):
    return cnt == required

def print_possible():
    print("Possible")

def print_impossible():
    print("Impossible")

def main():
    h, w = read_dimensions()
    grid = read_grid(h)
    cnt = count_hashes(grid)
    req = required_hash_count(h, w)
    if check_possible(cnt, req):
        print_possible()
    else:
        print_impossible()

main()