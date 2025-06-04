import sys

def main():
    for line in sys.stdin:
        if line.strip() == '':
            continue
        N, M = map(int, line.split())
        if N == 0 and M == 0:
            break

        packets = []
        for _ in range(M):
            t, s, d = map(int, sys.stdin.readline().split())
            packets.append((t, s, d))

        # Sort packets by timestamp
        packets.sort(key=lambda x: x[0])

        infected = [False] * (N + 1)
        infected[1] = True  # computer 1 is initially infected

        for t, s, d in packets:
            if infected[s]:
                infected[d] = True

        print(sum(infected))  # counts True since True == 1 in Python

if __name__ == "__main__":
    main()