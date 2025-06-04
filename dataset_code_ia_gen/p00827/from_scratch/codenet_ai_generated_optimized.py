def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

while True:
    a, b, d = map(int, input().split())
    if a == 0 and b == 0 and d == 0:
        break

    g, x0, y0 = extended_gcd(a, b)
    # Scale the solution to d/g
    x0 *= d // g
    y0 *= d // g

    # Coefficients for shifting solutions
    k1 = b // g
    k2 = a // g

    # Find t to minimize total weights x + y
    # x = x0 + k1 * t
    # y = y0 - k2 * t
    # sum = x + y = x0 + y0 + t*(k1 - k2)
    
    # Depending on sign of k1 - k2, choose t accordingly
    diff = k1 - k2

    # Candidate solutions to consider, as t integer values
    candidates = []

    # To keep x,y >= 0:
    # x0 + k1*t >= 0 => t >= -x0/k1 if k1 > 0
    # y0 - k2*t >= 0 => t <= y0/k2 if k2 > 0

    # Compute bounds on t to keep x,y nonnegative
    t_min = (-x0 + k1 - 1) // k1 if k1 != 0 else float('-inf')
    t_max = y0 // k2 if k2 != 0 else float('inf')

    # If k1 == 0 or k2 == 0, handle accordingly
    if k1 == 0:
        if x0 < 0:
            # no solution
            pass
        else:
            t_min = float('-inf')
    if k2 == 0:
        if y0 < 0:
            # no solution
            pass
        else:
            t_max = float('inf')

    # Because we want minimal x+y, which is sum = x0 + y0 + t*(k1 - k2)
    # If diff > 0, minimal sum at minimal t within bounds
    # If diff < 0, minimal sum at maximal t within bounds
    # If diff == 0, sum is constant, test all feasible t

    possible_t = []

    if diff > 0:
        # minimal sum at minimal feasible t
        # t_min and t_max can be bounds, but t integer
        t_candidate = t_min
        if t_candidate <= t_max:
            possible_t.append(t_candidate)
        else:
            # no t satisfying constraints?
            # try t_max if t_max >= t_min
            if t_max >= t_min:
                possible_t.append(t_max)
    elif diff < 0:
        # minimal sum at maximal feasible t
        t_candidate = t_max
        if t_candidate >= t_min:
            possible_t.append(t_candidate)
        else:
            if t_min <= t_max:
                possible_t.append(t_min)
    else:
        # diff==0 sum constant for all feasible t
        # try all feasible t in range t_min to t_max to find minimal total weight mass ax+by
        # to reduce complexity, try t_min, t_max and the integer t just to be sure

        # Clamp t_min and t_max inside reasonable limits
        if t_min == float('-inf'):
            t_min = -10**10
        if t_max == float('inf'):
            t_max = 10**10

        # We check t_min, t_max and t around zero since large extremes unlikely better
        checked_ts = {t_min, t_max, 0}

        # filter valid t in bounds
        possible_t = [t for t in checked_ts if t_min <= t <= t_max]

    best = None
    for t in possible_t:
        x = x0 + k1 * t
        y = y0 - k2 * t
        if x < 0 or y < 0:
            continue
        total = x + y
        mass = a * x + b * y
        if best is None or total < best[0] or (total == best[0] and mass < best[1]):
            best = (total, mass, x, y)

    # If no t found by previous logic, try searching around t_min to t_max for minimal sum and mass
    if best is None:
        # search t in range max(t_min, -100000) to min(t_max, 100000)
        start = max(t_min, -100000)
        end = min(t_max, 100000)
        for t in range(start, end+1):
            x = x0 + k1 * t
            y = y0 - k2 * t
            if x < 0 or y < 0:
                continue
            total = x + y
            mass = a * x + b * y
            if best is None or total < best[0] or (total == best[0] and mass < best[1]):
                best = (total, mass, x, y)

    print(best[2], best[3])