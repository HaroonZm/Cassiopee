import bisect

def read_case():
    """
    Reads a single case from standard input. First reads the number N.
    For N > 0, reads N records containing a string key and two integers for time values.
    Returns a dictionary mapping names to start times (as integer minutes since 00:00),
    or zero if N == 0 (which means end of input).
    """
    N = int(raw_input())
    if N == 0:
        return 0
    D = {}
    for i in range(N):
        # Read a line, split into tokens, first is the name, following two are integers
        inp = raw_input().split()
        # Map the time-related tokens to integers
        inp[1:] = map(int, inp[1:])
        name = inp[0]
        hour = inp[1]
        min_time = inp[2]
        # Calculate the start time in minutes (hour*60 + minutes extracted from min_time)
        stt = hour * 24 * 60 + (min_time // 100) * 60 + (min_time % 100)
        D[name] = stt
    return D

def read_reserved_keys(P):
    """
    Reads P reserved keys (names) from standard input and returns them as a list.
    """
    reserved_keys = []
    for i in range(P):
        name = raw_input()
        reserved_keys.append(name)
    return reserved_keys

def can_schedule_all(Tlist, P):
    """
    Checks the initial reserved schedule in Tlist for conflicts: ensures each reserved slot
    is at least 30 minutes apart from neighbors.
    Returns True if no conflicts found, False otherwise.
    """
    # The reserved times are from Tlist[1] to Tlist[P]
    for i in range(P+1):
        # If next time is within 30 minutes of previous, not valid
        if Tlist[i+1] < Tlist[i] + 30:
            print -1
            return False
    return True

def schedule_additional(D, Tlist, ans):
    """
    Attempt to greedily schedule other available times (from D.values()) into Tlist if there
    is a gap of at least 30 minutes on both sides for each new addition.
    Updates ans (the count of scheduled items).
    """
    # Get the list of remaining (unused) start times and sort them
    E = sorted(D.values())
    for st in E:
        # Find the insertion point for st in the sorted Tlist
        pos = bisect.bisect(Tlist, st)
        # Ensure that we can insert st, with at least 30 mins from neighbors
        if (st - Tlist[pos-1]) >= 30 and (Tlist[pos] - st) >= 30:
            ans += 1
            # Insert st into Tlist keeping it sorted
            bisect.insort(Tlist, st)
    print ans

def main():
    """
    Main function implementing the overall logic:
    - Continues reading cases until a 0 is encountered.
    - For each case, reads records, applies scheduling constraints,
      and prints the maximum number of non-conflicting scheduled times.
    """
    while True:
        D = read_case()
        if D == 0:
            break
        # Read the number of reserved slots
        P = int(raw_input())
        # Initialize the reserved time list with sentinels far outside possible values
        Tlist = [-99999999, 999999999]
        # Read the reserved slot names and extract start times, removing them from D
        reserved_keys = read_reserved_keys(P)
        for f in reserved_keys:
            Tlist.append(D.pop(f))
        # Sort the complete list of reserved times
        Tlist.sort()
        # Check for conflicts. If any, skip further scheduling for this case
        if can_schedule_all(Tlist, P):
            ans = P
            schedule_additional(D, Tlist, ans)

# Entry point of the script
if __name__ == '__main__':
    main()