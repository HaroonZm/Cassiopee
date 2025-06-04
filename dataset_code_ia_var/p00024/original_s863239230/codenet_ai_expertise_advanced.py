from sys import stdin

def compute_floors():
    for line in stdin:
        try:
            v_i = float(line)
            t = v_i / 9.8
            y = 4.9 * t * t
            yield int((y + 5) // 5 + 1)
        except ValueError:
            continue

if __name__ == "__main__":
    print('\n'.join(map(str, compute_floors())))