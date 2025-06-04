import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def angle_between_points(cx, cy, r, px, py):
    return math.atan2(py - cy, px - cx)

def normalize_angle(angle):
    while angle < 0:
        angle += 2 * math.pi
    while angle >= 2 * math.pi:
        angle -= 2 * math.pi
    return angle

def intervals_subtract(intervals, sub):
    result = []
    s_start, s_end = sub
    for (start, end) in intervals:
        if end <= s_start or start >= s_end:
            # no overlap
            result.append((start, end))
        else:
            # overlap exists, split
            if start < s_start:
                result.append((start, s_start))
            if end > s_end:
                result.append((s_end, end))
    return result

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    return merged

def complement_intervals(intervals):
    # intervals inside [0, 2pi), return parts not covered
    result = []
    if not intervals:
        return [(0, 2 * math.pi)]
    intervals = merge_intervals(intervals)
    if intervals[0][0] > 0:
        result.append((0, intervals[0][0]))
    for i in range(len(intervals)-1):
        result.append((intervals[i][1], intervals[i+1][0]))
    if intervals[-1][1] < 2 * math.pi:
        result.append((intervals[-1][1], 2 * math.pi))
    return result

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        circles = []
        for _ in range(n):
            x, y, r = map(float, input().split())
            circles.append((x, y, r))
        total_length = 0.0
        for i in range(n):
            cx, cy, cr = circles[i]
            covered_intervals = []
            for j in range(n):
                if i == j:
                    continue
                ox, oy, orr = circles[j]
                d = distance(cx, cy, ox, oy)
                if d >= cr + orr:
                    # no intersection
                    continue
                if d <= abs(cr - orr):
                    # one circle inside other
                    if cr <= orr:
                        # current circle completely inside other, no uncovered arc
                        covered_intervals = [(0, 2 * math.pi)]
                        break
                    else:
                        # other circle inside current, no effect on arc coverage
                        continue
                # calculate intersection angles on current circle
                # Law of cosines
                cos_angle = (cr*cr + d*d - orr*orr) / (2 * cr * d)
                if cos_angle < -1:
                    cos_angle = -1
                if cos_angle > 1:
                    cos_angle = 1
                angle_between_centers = math.atan2(oy - cy, ox - cx)
                angle_offset = math.acos(cos_angle)
                angle1 = normalize_angle(angle_between_centers - angle_offset)
                angle2 = normalize_angle(angle_between_centers + angle_offset)
                if angle2 < angle1:
                    # Interval crosses 0
                    covered_intervals.append((angle1, 2 * math.pi))
                    covered_intervals.append((0, angle2))
                else:
                    covered_intervals.append((angle1, angle2))
            # Merge intervals
            covered_intervals = merge_intervals(covered_intervals)
            # Calculate uncovered intervals
            uncovered_intervals = complement_intervals(covered_intervals)
            # Sum uncovered arcs length
            for start, end in uncovered_intervals:
                arc_length = cr * (end - start)
                total_length += arc_length
        print(total_length) 

main()