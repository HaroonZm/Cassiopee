from collections import deque

def main():
    """
    Main function to process a sequence of (time, value) events, maintaining a moving
    sum and computing time-weighted averages based on a sliding window sum "L".
    Each event either adds to the total, merges with previous events to not exceed
    "L", or removes oldest portions to keep the current total <= L.
    At each step, the time-weighted average for the last L units is computed.
    """

    # List to store time-weighted averages after each step
    TT_list = []

    # Read number of events N and the sum window L from input
    N, L = map(int, input().split())

    # Initialize aggregate variables
    vt_now = 0.0   # Current weighted sum (sum of t*v within buffer)
    v_now = 0      # Current sum of values within the buffer
    que = deque()  # Deque holding pairs [t, v] representing time and value contributions

    # Process each event
    for i in range(N):
        ti, v = map(int, input().split())
        t = float(ti)

        v_now += v        # Add current value to running total
        vt_now += v*t     # Add weighted contribution (v * t) to weighted sum

        # Case 1: Perfect fit, value fills the buffer exactly
        if v == L:
            que.append([t, v])
        else:
            # Merge current entry with previous entries until buffer doesn't overflow
            while v < L and len(que) > 0:
                t_last, v_last = que[-1]

                if t_last <= t:
                    # If the newest time is after the previous,
                    # simply append as a separate entry in buffer
                    que.append([t, v])
                    break
                elif v + v_last >= L:
                    # If sum would go above window size L, merge until sum is L
                    v_last = v + v_last - L
                    # Weighted average merge for perfect fit to L
                    t = ((L - v) * t_last + v * t) / L
                    v = L
                    que = deque([[t, v]])
                    v_now = L
                    vt_now = t * L
                    # We've filled the buffer perfectly, exit the merge loop
                else:
                    # Need to merge completely with the last entry
                    t = (t * v + t_last * v_last) / (v + v_last)
                    v = v + v_last
                    que.pop()

        # Case 2: Remove oldest contributions to keep buffer sum <= L
        while v_now > L:
            if que[0][1] <= v_now - L:
                # Oldest entry can be fully removed
                v_now -= que[0][1]
                vt_now -= que[0][1] * que[0][0]
                que.popleft()
            else:
                # Part of the oldest entry is removed
                reduction = v_now - L
                que[0][1] -= reduction
                vt_now -= reduction * que[0][0]
                v_now = L

        # Compute and store the current time-weighted mean for the buffer
        TT_list.append(vt_now / L)

    # Output the result
    for val in TT_list:
        print(val)

if __name__ == "__main__":
    main()