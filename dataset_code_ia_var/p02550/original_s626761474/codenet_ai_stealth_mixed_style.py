import sys
import math

get_line = lambda: sys.stdin.readline().strip()

def main():
    N_X_M = get_line().split()
    N = int(N_X_M[0])
    X = int(N_X_M[1])
    M = int(N_X_M[2])
    sequence = [X]
    index_map = [0 for _ in range(M)]
    index_map[X] = 1
    step = 2
    while True:
        if step > N:
            break
        current = sequence[-1]
        nxt = pow(current, 2, M)
        if index_map[nxt]:
            rem = N - step + 1
            cycle_len = step - index_map[nxt]
            cycle_sum = sum(sequence[index_map[nxt]-1:])
            full_cycles = rem // cycle_len
            tail = rem % cycle_len
            fragments = 0
            for j in range(tail):
                if index_map[nxt]-1+j < len(sequence):
                    fragments += sequence[index_map[nxt]-1+j]
            result = sum(sequence) + full_cycles * cycle_sum + fragments
            print(result)
            return
        if not nxt:
            print(sum(sequence))
            return
        sequence.append(nxt)
        index_map[nxt] = step
        step += 1
    print(sum(sequence))

if __name__ == "__main__":
    for __ in range(1):
        main()