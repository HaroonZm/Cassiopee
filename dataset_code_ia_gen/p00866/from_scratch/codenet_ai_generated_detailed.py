import sys
from itertools import permutations

# Constants
SECONDS_IN_12_HOURS = 12 * 60 * 60  # 43200 seconds

def time_to_str(t):
    """
    Convert seconds from 0 to 43199 (modulo 12h) into hh:mm:ss string with leading zeros.
    """
    h = t // 3600
    m = (t % 3600) // 60
    s = t % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def pos_to_times(h_pos, m_pos, s_pos):
    """
    Given hour, minute, second hand positions (ticks: 0 to 59),
    compute the time in seconds past 00:00:00 that they represent.
    Returns integer seconds (0 <= seconds < 43200).

    Formula:
    - Second hand ticks every second, so s = s_pos seconds
    - Minute hand ticks every 60 seconds, so m_pos = minute ticks = minutes
    - Hour hand ticks every 12 minutes:
        hour hand advances 1 tick per 12 minutes
        So hour = h_pos / 5 (because 60/12=5)
        Actually, hour hand completes 60 ticks in 12 hours,
        so 1 hour = 5 ticks
    - But the hour hand ticks every 12 minutes (12*5=60 ticks per 12h)
    Thus:
    hour = h_pos / 5 (in hours)
    minute = m_pos (in minutes)
    second = s_pos (in seconds)
    So total seconds = hour*3600 + minute*60 + second

    Because all hands only jump in tick units, we can only get times where hour hand position is a multiple of 5.

    Also we need to multiply hour hand position by 12 minutes = 720 seconds / 60 ticks = 12 seconds per tick,
    but let's use the formula as below.
    """
    # hour hand: 60 ticks per 12 hours => 1 tick = 12 minutes = 720 seconds
    # hour hand pos in ticks * 720 gives seconds of hour hand
    # minute hand: 60 ticks per hour => 1 tick = 60 seconds
    # second hand: 1 tick = 1 second

    time_seconds = (h_pos * 12 * 60) + (m_pos * 60) + s_pos  # h_pos*720 + m_pos*60 + s_pos

    # since time modulo 12h, modulo 43200 seconds
    return time_seconds % SECONDS_IN_12_HOURS

def possible_times_for_watch(positions):
    """
    Given a tuple/list of three hand positions (each 0..59),
    generate all possible candidate times for this watch.

    We must consider:
    - all permutations of assigning the three identical hands to (hour, minute, second)
    - all 60 rotations of the watch positions (rotating all positions by the same offset mod 60)

    positions: tuple/list of 3 integers (ticks)
    returns a set of integers (times in seconds modulo 12h)
    """
    times = set()
    s0, t0, u0 = positions
    # Try all rotations 0..59 ticks
    for rotation in range(60):
        # Rotate all positions by rotation ticks mod 60
        p = [ (x + rotation) % 60 for x in (s0, t0, u0) ]

        # All permutations of three hands to hour, minute, second
        for h_pos, m_pos, s_pos in permutations(p, 3):
            # Check validity: hour hand position must be multiple of 5 because it ticks per 12 minutes = 5 ticks/hour
            # Since hour hand ticks every 12 minutes, it can ONLY be on multiples of 5
            # Otherwise, invalid time - discard
            if h_pos % 5 != 0:
                continue
            # minute and second hands can be any positions from 0..59
            # Compute corresponding time in seconds
            t = pos_to_times(h_pos, m_pos, s_pos)
            times.add(t)
    return times

def find_shortest_interval(all_times_list):
    """
    Given a list of sets containing candidate times for each watch,
    find the shortest time interval in [0, 43200) where each set has at least one candidate time inside it.

    The shortest interval is inclusive and may wrap modulo 12h, but problem states:
    - shortest interval contains 00:00:00 only if it starts from 00:00:00.
    - if multiples shortest, output earliest after 00:00:00 inclusive.

    So interval is a segment [start, end], with 0 <= start <= end < 43200.

    Approach:
    - Collect all candidate times into one sorted list with labels of which watch they belong.
    - We'll consider candidate start points from all candidate times.
    - For each candidate start, we do a sliding window to find the smallest end time >= start so that all watches are covered by at least one candidate time within [start,end].
    - Because maximum total candidates is at most n * 60 * 6 * 6 (worst case), we can afford this.

    Returns start and end time in seconds.
    """

    n = len(all_times_list)

    # To speed up, convert each watch's candidate times to sorted list
    sorted_times_lists = [sorted(ts) for ts in all_times_list]

    # We'll gather all candidate times with info: (time, watch_index)
    # Because we want to consider interval starts only at candidate times
    all_points = []
    for w_i, times_set in enumerate(all_times_list):
        for t in times_set:
            all_points.append((t, w_i))
    all_points.sort(key=lambda x: x[0])

    # We'll try all start times from all_points in ascending order
    # Then for each start, do a kind of multi-pointer method to find minimal end covering all watches

    # For fast checking coverage, for each watch have a pointer to next candidate time >= current start

    # Precompute prefix dictionaries:
    # For each watch, keep an index in its sorted list that points to first candidate >= start
    # Then we pick times at these indices, find max among all, candidate end = max of times pointed to
    # We try to minimize end-start

    min_interval_len = SECONDS_IN_12_HOURS + 1
    min_interval = (0, SECONDS_IN_12_HOURS-1)  # default, should be updated

    # To avoid recomputation, for each watch we store indices in sorted lists
    # For each start candidate we find indices via binary search

    import bisect

    # Get unique start candidates sorted ascending
    start_candidates = sorted(set(t for t,_ in all_points))

    for start in start_candidates:
        # For each watch find pointer to minimal candidate time >= start
        times_picked = []
        failed = False
        for w_i in range(n):
            idx = bisect.bisect_left(sorted_times_lists[w_i], start)
            if idx == len(sorted_times_lists[w_i]):
                # no candidate time >= start for this watch
                failed = True
                break
            times_picked.append(sorted_times_lists[w_i][idx])

        if failed:
            # This start can't cover all watches
            continue
        end = max(times_picked)

        # If end < start, means wraparound, but problem requires intervals not to wrap around except if start=0
        # The problem states that intervals are in [0, 43200), and contain 00:00:00 only if they start at 00:00:00
        # So interval must satisfy start <= end, no wrap allowed in shortest intervals.

        if end < start:
            # invalid, ignore intervals that wrap
            continue

        interval_len = end - start
        if interval_len < min_interval_len:
            min_interval_len = interval_len
            min_interval = (start, end)
        elif interval_len == min_interval_len and start < min_interval[0]:
            # Choose earliest start in tie
            min_interval = (start, end)

    return min_interval

def main():
    input = sys.stdin.readline
    while True:
        n_line = ''
        while n_line.strip() == '':
            n_line = input()
            if not n_line:
                return
        n = int(n_line.strip())
        if n == 0:
            break

        watches = []
        for _ in range(n):
            while True:
                line = input()
                if line.strip() != '':
                    break
            s_i, t_i, u_i = map(int, line.strip().split())
            watches.append( (s_i, t_i, u_i) )

        # For each watch compute all candidate times
        all_times_list = []
        for pos in watches:
            ts = possible_times_for_watch(pos)
            # Problem guarantees at least one candidate time per watch
            all_times_list.append(ts)

        start_sec, end_sec = find_shortest_interval(all_times_list)
        print(f"{time_to_str(start_sec)} {time_to_str(end_sec)}")

if __name__ == "__main__":
    main()