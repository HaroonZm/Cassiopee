def read_input():
    return input().split()

def should_stop(r):
    return r == "0"

def count_hits(r, a):
    hit = 0
    for x, y in zip(r, a):
        if x == y:
            hit += 1
    return hit

def count_blow(r, a):
    blow = -count_hits(r, a)
    for x in r:
        if x in a:
            blow += 1
    return blow

def print_result(hit, blow):
    print(hit, blow)

def main_loop():
    while True:
        r, a = read_input()
        if should_stop(r):
            break
        hit = count_hits(r, a)
        blow = count_blow(r, a)
        print_result(hit, blow)

main_loop()