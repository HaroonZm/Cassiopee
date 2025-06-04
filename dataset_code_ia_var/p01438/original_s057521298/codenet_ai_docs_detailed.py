from collections import defaultdict

def process_input():
    """
    Processes multiple test cases until a zero is encountered.
    For each test case:
        - Reads the number of men
        - For each man, reads their work intervals and computes their scheduled times as bitmasks
        - Computes the maximum total efficiency by selecting non-overlapping schedules
    
    Side effect: prints the maximum total efficiency for each test case.
    """
    while True:
        n = int(raw_input())
        if n == 0:
            break

        # List to store the efficiency of each man
        efficiency_list = [0] * n
        # List to store the time schedule bitmask for each man
        schedule_masks = [0] * n

        # Read the schedule for each man
        for man_index in xrange(n):
            m, l = map(int, raw_input().split())
            efficiency_list[man_index] = l
            schedule_mask = 0
            for _ in xrange(m):
                # s: start hour, e: end hour (exclusive)
                s, e = map(int, raw_input().split())
                # For this range, mark all hours from (s-6) to (e-6) as occupied in the bitmask
                for hour in xrange(s-6, e-6):
                    schedule_mask |= 1 << hour
            schedule_masks[man_index] = schedule_mask

        # dp[i][mask] represents the maximum efficiency achievable 
        # using men up to index 'i' with the set of used times described by 'mask'
        dp = [defaultdict(int) for _ in xrange(n)]
        dp[0][schedule_masks[0]] = efficiency_list[0]

        for i in xrange(1, n):
            for curr_mask in dp[i-1].keys():
                # If the current man's schedule does not conflict with curr_mask:
                if curr_mask & schedule_masks[i] == 0:
                    # Option 1: add this man (combine masks)
                    combined_mask = curr_mask | schedule_masks[i]
                    dp[i][combined_mask] = max(dp[i][combined_mask], dp[i-1][curr_mask] + efficiency_list[i])
                # Option 2: skip this man
                dp[i][curr_mask] = max(dp[i][curr_mask], dp[i-1][curr_mask])
            # Also consider the situation where only this man is selected
            dp[i][schedule_masks[i]] = max(dp[i][schedule_masks[i]], efficiency_list[i])

        # Find the maximum efficiency for this test case
        max_efficiency = max(max(masked_values.values()) for masked_values in dp)
        print max_efficiency

# Start processing
process_input()