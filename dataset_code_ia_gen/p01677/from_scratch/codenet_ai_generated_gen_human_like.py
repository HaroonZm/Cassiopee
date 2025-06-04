def check_signal(arr, val):
    n = len(arr)
    used_val_indices = []
    for i in range(n):
        if arr[i] == 'x':
            continue
        if not isinstance(arr[i], int):
            continue
    # substitute broken samples with val
    signal = []
    for x in arr:
        if x == 'x':
            signal.append(val)
        else:
            signal.append(x)
    # check the conditions
    for i in range(n):
        left = signal[i-1] if i-1 >= 0 else None
        right = signal[i+1] if i+1 < n else None
        cur = signal[i]
        if (i+1) % 2 == 1:  # odd-indexed sample (1-based)
            # value must be strictly smaller than neighbors
            if left is not None and cur >= left:
                return False
            if right is not None and cur >= right:
                return False
        else:  # even-indexed sample (1-based)
            # value must be strictly larger than neighbors
            if left is not None and cur <= left:
                return False
            if right is not None and cur <= right:
                return False
    return True

def find_possible_values(arr):
    fixed = [x for x in arr if x != 'x']
    if not fixed:
        # all samples broken, can try all values? no constraints
        # but must satisfy the pattern: odd samples < neighbors and even samples > neighbors
        # with all equal values for broken samples, so all values equal val
        # can this pattern be satisfied by a constant array? No, since neighbors differ
        # so no possible value
        return set()

    min_val = -10**9
    max_val = 10**9

    # gather adjacent known values to derive bounds on val
    n = len(arr)

    # We'll attempt to find the range of val that satisfies the constraints from neighbors

    # Because all broken values are equal, the problem reduces to the constraints derived from neighbors near broken positions

    # For positions where arr[i] == 'x', neighbors influence possible val

    # We'll store inequalities of the form val < neighbor_val or val > neighbor_val or val < val or val > val

    # Since neighbors can be x or known. If neighbors are x, then val == val, so no info.

    # So only neighbors with known values impose constraints

    # We will construct lower and upper bounds for val

    # Lower bound initial -inf and upper bound +inf but here as numbers large but finite

    lower = -10**18
    upper = 10**18

    for i in range(n):
        if arr[i] == 'x':
            idx = i + 1  # 1-based index
            val_pos = idx
            left_val = arr[i-1] if i-1 >= 0 else None
            right_val = arr[i+1] if i+1 < n else None

            if val_pos % 2 == 1:
                # odd sample < neighbors
                # val < left_val if left_val known
                if left_val is not None and left_val != 'x':
                    # val < left_val
                    upper = min(upper, left_val - 1)
                # val < right_val if right_val known
                if right_val is not None and right_val != 'x':
                    upper = min(upper, right_val - 1)
            else:
                # even sample > neighbors
                # val > left_val if left_val known
                if left_val is not None and left_val != 'x':
                    lower = max(lower, left_val + 1)
                # val > right_val if right_val known
                if right_val is not None and right_val != 'x':
                    lower = max(lower, right_val + 1)

    # After bounds established, must verify for existing known x positions that have neighbors x too

    # Next, also check the positions that are known and adjacent to 'x' to guarantee uniqueness

    # If no 'x' at all, just check validity (but problem states broken samples so always at least one)

    # Check if a value exists in [lower, upper] and also check if exactly one possible val in this integer range satisfies check_signal

    candidates = []
    for val in range(max(lower, -10**9), min(upper, 10**9)+1):
        if check_signal(arr, val):
            candidates.append(val)
            if len(candidates) > 1:
                return "ambiguous"

    if len(candidates) == 0:
        return "none"
    else:
        return candidates[0]

def main():
    import sys
    input = sys.stdin.readline

    while True:
        N = input()
        if not N:
            break
        N = N.strip()
        if N == '0':
            break
        N = int(N)
        line = ''
        while line.strip() == '':
            line = input()
        arr = line.strip().split()
        # convert known integers to int
        for i in range(len(arr)):
            if arr[i] != 'x':
                arr[i] = int(arr[i])
        res = find_possible_values(arr)
        print(res)

if __name__ == '__main__':
    main()