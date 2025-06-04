import sys

def base36encode(num):
    # Convert an integer 0 <= num < 36 to the corresponding base36 character
    if 0 <= num <= 9:
        return chr(ord('0') + num)
    else:
        return chr(ord('A') + (num - 10))

def solve_dataset(N, M, Q, operations):
    # N = number of switches
    # M = number of bulbs
    # Q = number of operations
    # operations: list of tuples (S_i, B_i), S_i and B_i are strings with '0' and '1'

    # We'll reconstruct the correspondence between switches and bulbs as an M-length array.
    # Each bulb j is controlled by exactly one switch i: bulb_state_j = switch_state_i (XOR count of toggles mod 2).
    # Operation: toggled switches are XORed with current switch state.
    # The bulb state after operations reflects parity of toggles on controlling switch.

    # Let's denote variables:
    # Let s be the vector of switch states (initially zero vector length N)
    # Each bulb j corresponds to a vector w_j in GF(2)^N representing which switch controls it.
    # Since each bulb is controlled by exactly one switch, w_j is a one-hot vector => only one bit set.

    # At each operation:
    # s_new = s_old XOR S_i
    # bulbs state after operation = XOR over bulbs controlled by switches that have been toggled odd number of times:
    # i.e. bulb_state_j = dot_product(w_j, s_new) mod 2  (since bulb toggles whenever its switch toggled)
    #
    # For each bulb j and operation i:
    # B_i[j] = parity of toggles on the switch controlling j after operation i, i.e. B_i[j] = s_i[the unique bit set in w_j].

    # The input gives a sequence of s_i (cumulative toggled switches) and B_i (bulb states):
    # We want to find for each bulb j the index k of the switch that controls it,
    # such that for each operation i: B_i[j] = s_i[k].

    # Algorithm:
    # 1. We read operations:
    #    For i in [0,Q-1], s_i = XOR of all switches toggled so far (each S_i line is toggled switches, cumulative s_i = s_(i-1) XOR S_i).
    #    But problem states the state of switches and bulbs is kept after each operation.
    #    The input line for operation i is S_i (switches toggled this operation), B_i (bulbs states after operation).
    #
    # 2. We reconstruct s_i (switches states after i-th operation):
    #    s_0 = 0 (all off)
    #    s_1 = s_0 XOR S_1
    #    s_2 = s_1 XOR S_2
    #    ...
    #
    # 3. For each bulb j, we want to find the unique switch index k such that for all i:
    #    B_i[j] == s_i[k]
    #
    # 4. For each bulb, find all possible switches k that satisfy this equality over all operations i:
    #     For each switch k, check if for all i (0 to Q-1), B_i[j] == s_i[k].
    # 5. If exactly one k matches, output that switch in base36.
    #    Else output '?'.

    # Note: Q can be zero: then no info about togglings: all bulbs off => ambiguous.
    #       M can be large, up to 1000. N up to 36. Q up to 1000.

    # Implementation details:

    # We'll store s_i as list of length Q, each s_i is a bitstring of length N.
    # To speed up, store s_i as integer bitmasks for switches states.

    # For bulbs, we'll store B_i as list of strings (or better: as list of integer bitmasks over bulbs for each operation).
    # But since M can be 1000, storing bitmasks as integers is inefficient (would need multiple ints).
    # So just keep B_i as list of strings for bulbs states.

    # For checking per bulb:
    #   For each bulb j:
    #     For each switch k:
    #       Check if for all i, B_i[j] == bit of s_i at k-th switch
    #     Store possible matches for bulb j.
    #   Result depends if unique or ambiguous.

    # Pre-processing:
    # - For each operation i, parse S_i and accumulate s_i.
    # - For each switch k, for i in [0,Q-1], extract bit s_i[k]
    #   -> For quick checking, we can pre-store these bits as a list: For switch k: list of Q bits s_i[k].

    # - For each bulb j, collect bits B_i[j], check against each switch k bit array.

    # Return a string of length M representing the switch for each bulb or '?'.

    # Step 1: parse operations and accumulate s_i (switch states)
    s_states = []
    current_s = 0  # bitmask of switches state
    for i in range(Q):
        S_i_str, B_i_str = operations[i]
        # S_i: toggled switches (string of length N)
        # convert to bitmask:
        toggled = 0
        for idx, ch in enumerate(S_i_str):
            if ch == '1':
                toggled |= 1 << (N-1 - idx)
        current_s ^= toggled
        s_states.append(current_s)

    # Step 2: For each switch k, build array bits over Q ops: s_states[i][k]
    # We'll store for each switch k an array of bits: bit i indicates if the switch k was on at operation i
    switch_bits = []
    for k in range(N):
        bits = []
        mask = 1 << (N-1 - k)
        for i in range(Q):
            bits.append(1 if (s_states[i] & mask) else 0)
        switch_bits.append(bits)

    # Step 3: For each bulb j, get B_i[j] bits for all i (length Q)
    # Then find all switches k that match all i:
    # B_i[j] == switch_bits[k][i] for all i in 0..Q-1
    # If multiple or zero switch matches, output '?'

    result = []
    # For Q=0, no info, all bulbs ambiguous
    if Q == 0:
        return '?' * M

    # To speed up, transposing B_i to get bulbs data for all operations:
    # bulbs_data[j] = list of bits over Q operations
    bulbs_data = []
    for j in range(M):
        bits = []
        for i in range(Q):
            bits.append(int(operations[i][1][j]))
        bulbs_data.append(bits)

    for j in range(M):
        b_bits = bulbs_data[j]
        candidates = []
        for k in range(N):
            # check if for all i: b_bits[i] == switch_bits[k][i]
            match = True
            sb = switch_bits[k]
            # compare lists
            for x in range(Q):
                if b_bits[x] != sb[x]:
                    match = False
                    break
            if match:
                candidates.append(k)
                if len(candidates) > 1:
                    break
        if len(candidates) == 1:
            # unique switch, output in base36
            result.append(base36encode(candidates[0]))
        else:
            # ambiguous
            result.append('?')

    return ''.join(result)


def main():
    input = sys.stdin.readline
    while True:
        line = ''
        # skip empty lines if any
        while line.strip() == '':
            line = sys.stdin.readline()
            if line == '':
                return  # EOF
        N, M, Q = map(int, line.strip().split())
        if N == 0 and M == 0 and Q == 0:
            break
        operations = []
        for _ in range(Q):
            while True:
                line = sys.stdin.readline()
                if line.strip() != '':
                    break
            S_i, B_i = line.strip().split()
            operations.append((S_i, B_i))
        ans = solve_dataset(N, M, Q, operations)
        print(ans)


if __name__ == "__main__":
    main()