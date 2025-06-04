import sys

def base36(n):
    if n < 10:
        return chr(ord('0') + n)
    return chr(ord('A') + n - 10)

def solve():
    input = sys.stdin.readline
    while True:
        N, M, Q = map(int, input().split())
        if N == 0 and M == 0 and Q == 0:
            break
        S_list = []
        B_list = []
        for _ in range(Q):
            S, B = input().split()
            S_list.append(int(S, 2))
            B_list.append(B)
        # For each bulb, set of possible controlling switches (as a bitmask of length N)
        possible = [(1<<N)-1 for _ in range(M)]

        # Current switch states (bitmask)
        switch_state = 0
        # Current bulb states (list of int)
        bulb_state = [0]*M

        for i in range(Q):
            Si = S_list[i]
            Bi = B_list[i]
            # Update switches state
            switch_state ^= Si
            # For each bulb -> bulb_state[j] ^ operated switches on controlling switch == Bi[j]
            # Because bulb state toggles if controlling switch is flipped
            # For bulb j that is controlled by switch k (one switch only), bulb_state[j] ^ ((switch_state>>k)&1) == int(Bi[j])

            for j in range(M):
                expected = int(Bi[j])
                actual = bulb_state[j] ^ ((switch_state) & 0)
                # Since each bulb controlled by exactly one switch,
                # we check for each possible switch if with that switch toggled or not the bulb matches expected.
                # Filter possible switches for this bulb accordingly.

                # We can note: for switch k controlling bulb j:
                # bulb_state[j] ^ ((switch_state >> k) & 1) == expected
                # => ((switch_state >> k) &1) == bulb_state[j]^expected
                # For each possible switch k, check if bit k of switch_state equals bulb_state[j]^expected
                val = bulb_state[j] ^ expected
                mask = 0
                for k in range(N):
                    if ((switch_state >> k) & 1) == val:
                        mask |= (1 << k)
                possible[j] &= mask
            # Update bulb_state for next iteration
            for j in range(M):
                bulb_state[j] = int(Bi[j])

        # Now we have for each bulb possible switches controlling it
        # Each bulb is controlled by exactly one switch
        # Try to deduce unique assignment where possible
        # Such problem is like n variables, each variable domain possible[j]
        # We can use constraint propagation:
        # If a switch assigned uniquely to a bulb, remove it from others

        changed = True
        while changed:
            changed = False
            assigned = [p for p in possible if bin(p).count("1")==1]
            assigned_switches = 0
            for p in assigned:
                assigned_switches |= p
            for j in range(M):
                if bin(possible[j]).count("1") > 1:
                    # Remove assigned switches from other bulbs
                    new_possible = possible[j] & (~assigned_switches)
                    if new_possible != possible[j]:
                        possible[j] = new_possible
                        changed = True

        # Output results
        res = []
        for p in possible:
            c = '?'
            if bin(p).count("1")==1:
                idx = (p & -p).bit_length() -1
                c = base36(idx)
            res.append(c)
        print("".join(res))

if __name__ == "__main__":
    solve()