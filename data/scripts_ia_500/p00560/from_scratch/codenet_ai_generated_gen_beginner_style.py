N, M, K = map(int, input().split())
A, B, C = map(int, input().split())
T = int(input())
stops = [int(input()) for _ in range(M)]

# On each segment between express stops, semiexpress stops must be chosen
# We try to insert semiexpress stops greedily to maximize reachable stations

# We consider sections between express stops:
sections = []
for i in range(M - 1):
    sections.append((stops[i], stops[i+1]))

# The semiexpress stops include all express stops plus K-M others between them
# We'll try to add semiexpress stops to minimize travel time to stations

# For each station, the fastest way is min over:
# all reachable express/semiexpress stops j <= station s:
# time = sum of edges by express/semiexpress + local from stop j to s

# Because N can be very large, we cannot simulate all stations
# Instead, we consider that segments between stops are uniform

# We pick semiexpress stops such that they subdivide the intervals between express stops

# The approach is:
# - Distribute K - M stops over the M-1 intervals between express stops
# - For each interval, number of extra stops = x
# - So interval is subdivided into x+1 parts, each part traveled by semiexpress
#   travel time per edge in semiexpress is C
#   local train travel is A
#   express train per edge is B (fastest)
# - Then reachable stations from the left stop in this interval 
#   within T can be computed for each interval

# We do binary search on how to distribute extra stops to maximize count

# Since constraints are tight, do simple uniform allocation (first approach)

# number of extra semiexpress stops to allocate is K - M
extra = K - M

# We will assign extra stops equally as possible to each interval
base = extra // (M -1)
rem = extra % (M -1)

semiexpress_counts = [base] * (M -1)
for i in range(rem):
    semiexpress_counts[i] +=1

# Calculate reachable stations considering each interval independently and summing

result = 0

for idx in range(M -1):
    left = stops[idx]
    right = stops[idx+1]
    length = right - left
    count_semi = semiexpress_counts[idx] +1  # Number of segments in this interval by semiexpress
    # length edges split into count_semi segments, each segment length:
    seg_len = length / count_semi

    # Time to go from left stop to station s in [left+1, right]
    # Min time is achieved by first going to closest semiexpress stop left or right of s
    # Actually, stops of semiexpress are equally spaced
    
    # For each station in interval:
    # Time to reach station s = min over semiexpress stops j:
    # Time from left to stop j by semiexpress: (distance in segments) * C
    # Then from j to s by local train: (abs(s-j)) * A

    # To simplify, maximum time among stations is to farthest station:
    # Because we want number of stations reachable within T,
    # we try to count stations in this interval reachable

    # To avoid going station by station (too large), we check reachable number of stations based on time

    # The worst case is when station is in middle between two semiexpress stops

    # Max distance from semiexpress stop to station is floor(seg_len)

    # So, max time from left stop to station is:
    # semiexpress travel time = (segment index)*C
    # local travel time = <= floor(seg_len)*A

    # To count reachable stations, we consider stations reachable if:
    # time from station 1 to semiexpress stop + local remainder <= T

    # Travel time from station 1 to left semiexpress stop is not considered here, but same for all intervals

    # For simplicity, consider stations reachable if after traveling from left stop using semiexpress + local time <= remaining T

    # Calculate total reachable stations in interval assuming traveling from left stop
    # To be more conservative, assume can reach up to a distance D where D*C + (seg_len)*A <= T_left
    # But T_left depends on previous intervals.

    # Because we start at station 1, which is stops[0], total travel is sum of interval times

    # Since problem is complex, we do approximation:
    # Can't simulate large N, so approximate number of stations reachable in interval as min(length, max_stations_in_time)

    # Maximum stations reachable by local train from station 1 directly (slowest):
    max_local = 0
    # We will not use local train from station 1 directly for all stations, but as fallback

total_result = 0
time_used = 0
for idx in range(M -1):
    left = stops[idx]
    right = stops[idx+1]
    length = right - left
    count_semi = semiexpress_counts[idx] +1
    seg_len = length / count_semi

    # We want to find number of stations reachable in this interval given time T - time_used so far

    # For each segment, time across semiexpress edges is (count_semi -1)* C  (between stops)

    # Because traveling via semiexpress between stops length each seg_len:

    semiexpress_time = (count_semi -1) * seg_len * C

    # The semiexpress stops are included

    # The local train covers at most seg_len stations per segment

    # For approximation, we find maximum local steps reachable after semiexpress travel

    # Let's find max local stations reachable in interval after semiexpress travel:

    max_local_stations = 0

    # For each segment, local time max is (seg_len) * A
    # We can reach some stations outside semiexpress stops by local train if time allows

    # Time to reach station s in this interval is:
    # semiexpress travel to closest semiexpress stop + local travel <= T - time_used

    # The farthest station from semiexpress stop is seg_len (at most)
    # So max local travel time = seg_len * A

    remaining_time = T - time_used
    if remaining_time < 0:
        break

    # Maximum number of stations reachable via semiexpress + local:
    # For each segment:
    # total_time to farthest local station is:
    # segment_length * C + segment_length * A (worst case)
    # But semiexpress travel is only between semiexpress stops, so max semiexpress travel in interval:
    semi_time = (count_semi -1) * seg_len * C
    # max local time per segment:
    max_local_time_per_segment = seg_len * A

    # Total max time from left stop to right stop:
    total_interval_time = semi_time + max_local_time_per_segment

    if total_interval_time <= remaining_time:
        # can reach all stations in interval
        reachable_stations = length
    else:
        # partial stations reachable
        # Let's try to binary search how many stations reachable in interval

        # Number stations between left and right: length

        # For approximation, we consider worst case:

        # time to reach k stations after left stop:
        # travel by semiexpress along segments + local train to station

        # We want to find maximum s in [0,length] so that
        # time from left to station s <= remaining_time

        # time from left to station s:
        # find position of nearest semiexpress stop

        # For simplicity assume station s is in segment seg_idx = int(s / seg_len)

        # distance from left to semiexpress stop in semiexpress edges:
        # seg_idx * seg_len

        # semiexpress time: seg_idx * seg_len * C

        # local time: (s - seg_idx*seg_len) * A

        # total time = semiexpress time + local time <= remaining_time

        # since s - seg_idx*seg_len <= seg_len

        # Let's try all segments and find max s

        max_s = 0
        for seg_idx in range(count_semi):
            # For stations in segment seg_idx:
            # max station in this segment is min(length, (seg_idx+1)*seg_len)

            left_bound = seg_idx * seg_len
            right_bound = min(length, (seg_idx+1)*seg_len)

            # time for stations in this segment:
            # time(s) = seg_idx * seg_len * C + (s - seg_idx*seg_len)* A <= remaining_time

            # solve for s:

            max_station_in_seg = int((remaining_time - seg_idx * seg_len * C)/A + seg_idx*seg_len)

            if max_station_in_seg >= left_bound:
                reachable_in_seg = min(int(right_bound), max_station_in_seg) - int(left_bound) + 1
                if reachable_in_seg > 0:
                    max_s = max(max_s, int(left_bound) + reachable_in_seg -1)

        reachable_stations = max(0,min(length, max_s))

    total_result += reachable_stations
    time_used += (length * B)  # approximate move to next interval by express (fastest)

print(total_result)