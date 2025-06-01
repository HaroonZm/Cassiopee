# Ok, so this is a DP solution, but I've tried to tweak it a bit, added some comments where I thought it'd help.
# Might be a bit inconsistent in style and spacing because, well, who writes perfectly neat code all the time?

bit_counts = [bin(x).count('1') for x in range(65536)]  # precompute bit counts for all 16-bit nums

def solve():
    import sys
    input_stream = sys.stdin
    
    while True:
        line = input_stream.readline()
        if not line:
            break
        n, c = map(int, line.split())
        if n == 0:
            break
        
        # read pattern A
        A = []
        for _ in range(n):
            # input has spaces between bits, so remove them and convert to int base 2
            bits_line = input_stream.readline().strip().replace(" ", "")
            A.append(int(bits_line, 2))
        
        # read pattern B
        B = []
        for _ in range(c):
            bits_line = input_stream.readline().strip().replace(" ", "")
            B.append(int(bits_line, 2))
        
        dp_current = {A[0]: 0}  # dict: state -> max score
        dp_next = {}
        
        # process each A except the first, then one extra iteration with 0
        for a in A[1:] + [0]:
            for state, score_so_far in dp_current.items():
                for b_pattern in B:
                    common_bits = state & b_pattern
                    new_score = score_so_far + bit_counts[common_bits]
                    new_state = (state - common_bits) | a
                    # update dp_next for new_state if better
                    if new_state not in dp_next or dp_next[new_state] < new_score:
                        dp_next[new_state] = new_score
            dp_current, dp_next = dp_next, {}
        
        # output the best achievable score for any state
        print(max(dp_current.values()))

# run the solve function
solve()