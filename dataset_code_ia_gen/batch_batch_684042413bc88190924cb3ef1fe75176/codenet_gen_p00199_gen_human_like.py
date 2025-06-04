def main():
    import sys

    def seat_A(chairs):
        for i in range(len(chairs)):
            if chairs[i] == '#':
                return i
        return -1  # Should not happen

    def seat_B(chairs):
        n = len(chairs)
        # Find seats not adjacent to A from right to left
        candidates = []
        for i in reversed(range(n)):
            if chairs[i] == '#':
                left_A = (i > 0 and chairs[i - 1] == 'A')
                right_A = (i < n - 1 and chairs[i + 1] == 'A')
                if not (left_A or right_A):
                    candidates.append(i)
        if candidates:
            return candidates[0]
        else:
            # No place except next to A, so pick leftmost empty seat from left
            for i in range(n):
                if chairs[i] == '#':
                    return i
        return -1  # Should not happen

    def seat_C(chairs):
        n = len(chairs)
        occupied_positions = [i for i, c in enumerate(chairs) if c != '#']
        if not occupied_positions:
            # No one seated yet, seat in middle
            if n % 2 == 1:
                return (n + 1) // 2 - 1
            else:
                return n // 2
        # For each seated person from left to right
        for pos in occupied_positions:
            # Try right neighbor
            r = pos + 1
            if r < n and chairs[r] == '#':
                return r
            # Try left neighbor
            l = pos - 1
            if l >= 0 and chairs[l] == '#':
                return l
        # If none found, seat in middle (same rule as above)
        # But problem states tries next people's neighbors accordingly, so should always sit next to someone if possible
        # just in case, fallback:
        if n % 2 == 1:
            return (n + 1) // 2 - 1
        else:
            return n // 2

    def seat_D(chairs):
        n = len(chairs)
        occupied_positions = [i for i, c in enumerate(chairs) if c != '#']
        if not occupied_positions:
            return 0  # seat left end if no one seated
        max_dist = -1
        candidates = []
        for i in range(n):
            if chairs[i] != '#':
                continue
            # Distance to nearest occupied
            dist = min(abs(i - pos) for pos in occupied_positions)
            if dist > max_dist:
                max_dist = dist
                candidates = [i]
            elif dist == max_dist:
                candidates.append(i)
        # If max_dist == 0, have to sit adjacent to someone, choose leftmost among them
        return candidates[0]

    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        line=line.strip()
        if not line:
            continue
        n_m = line.split()
        if len(n_m) != 2:
            continue
        n, m = map(int, n_m)
        if n == 0 and m == 0:
            break
        passengers = []
        for _ in range(m):
            passengers.append(input().strip())
        chairs = ['#'] * n
        for p in passengers:
            if p == 'A':
                pos = seat_A(chairs)
                chairs[pos] = 'A'
            elif p == 'B':
                pos = seat_B(chairs)
                chairs[pos] = 'B'
            elif p == 'C':
                pos = seat_C(chairs)
                chairs[pos] = 'C'
            else:  # D
                pos = seat_D(chairs)
                chairs[pos] = 'D'
        print(''.join(chairs))


if __name__ == "__main__":
    main()