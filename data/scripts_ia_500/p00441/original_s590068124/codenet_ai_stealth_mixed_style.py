def input_int():
    return int(input())

def get_poles(n):
    poles_list = []
    for _ in range(n):
        poles_list.append(tuple(map(int, input().split())))
    return poles_list

def has_square(poles, poles_set):
    max_sq = 0
    for i in range(len(poles)):
        x1, y1 = poles[i]
        for j in range(i, len(poles)):
            x2, y2 = poles[j]
            dx, dy = x2 - x1, y2 - y1
            cond1 = (x2 + dy, y2 - dx) in poles_set and (x1 + dy, y1 - dx) in poles_set
            cond2 = (x2 - dy, y2 + dx) in poles_set and (x1 - dy, y1 + dx) in poles_set
            if cond1 or cond2:
                dist_sq = dx*dx + dy*dy
                if dist_sq > max_sq:
                    max_sq = dist_sq
    return max_sq

def main():
    from sys import stdin
    inputs = stdin.read().strip().split()
    idx = 0
    while True:
        if idx >= len(inputs):
            break
        n = int(inputs[idx])
        idx += 1
        if n == 0:
            break
        poles = [ (int(inputs[idx+2*i]), int(inputs[idx+2*i+1])) for i in range(n)]
        idx += 2*n
        poles_set = set(poles)
        print(has_square(poles, poles_set))

if __name__ == "__main__":
    main()