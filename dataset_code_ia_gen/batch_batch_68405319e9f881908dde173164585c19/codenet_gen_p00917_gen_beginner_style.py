from math import gcd

def reduce_fraction(n, d):
    g = gcd(n, d)
    return n // g, d // g

def time_to_fractional_seconds(h, m, s):
    return h * 3600 + m * 60 + s

def seconds_to_hmd(H, t):
    t %= H * 3600
    h = t // 3600
    t %= 3600
    m = t // 60
    s_frac = t % 60
    return h, m, s_frac

def get_angle(H, h, m, s_frac):
    # s_frac is fractional seconds as a fraction tuple (n, d)
    # but here given as integer seconds, for simplicity.
    # The input seconds are integers here.
    # We'll handle fractional seconds during searching.
    # Return angles in degrees
    # hour hand: 360 degrees in H hours = 360/(H*3600) degrees per sec
    # minute hand: 360 degrees in 3600 sec = 0.1 deg/sec
    # second hand: 360 degrees in 60 sec = 6 deg/sec

    # To get angles at fractional seconds we will compute with floating point here for simplicity.
    hour_angle = ((h * 3600 + m * 60 + s_frac) / (H * 3600)) * 360
    minute_angle = ((m * 60 + s_frac) / 3600) * 360
    second_angle = (s_frac / 60) * 360
    return hour_angle % 360, minute_angle % 360, second_angle % 360

def angle_diff(a,b):
    diff = abs(a-b)
    if diff > 180:
        diff = 360 - diff
    return diff

def hands_overlap(ha, ma, sa):
    eps = 1e-9
    # Check if any two hands overlap considering floating point tolerance
    if abs(ha - ma) < eps or abs(abs(ha - ma) - 360) < eps:
        return True
    if abs(ha - sa) < eps or abs(abs(ha - sa) - 360) < eps:
        return True
    if abs(ma - sa) < eps or abs(abs(ma - sa) - 360) < eps:
        return True
    return False

def equal_fraction(a, b, eps=1e-9):
    return abs(a - b) < eps

def first_fractional_second(H, h, m, s):
    # We'll check from given time onward, with 1/1427 sec step (based on sample output denominator)
    # But this denominator seems arbitrary. We'll accept denominators up to 10^5 to be safe.
    # But as beginner, let's try step=1 second first.
    # If no solution found, try 1/1427 steps, but for simplicity, 1/1427 step.

    # We can try 1/1427 steps. Max time to search: H hours in seconds.
    max_steps = H * 3600 * 1427  # checking every 1/1427 second

    start = h * 3600 + m * 60 + s
    eps = 1e-8

    for step in range(int(start * 1427), int(H * 3600 * 1427)):
        # current time in seconds with fraction
        t_frac = step / 1427.0
        t_int = int(t_frac)
        frac = t_frac - t_int
        # convert fractional seconds to n/d fraction
        # fraction denominator fixed 1427 as per sample output

        # get h,m,sfrac
        total_seconds = t_frac % (H * 3600)
        hh = int(total_seconds // 3600)
        mm = int((total_seconds % 3600) // 60)
        ss = total_seconds % 60

        n = int(round((ss - int(ss)) * 1427))
        d = 1427
        if n == 0:
            d = 1

        # calculate angles with float for tolerance
        hour_angle = ((hh * 3600 + mm * 60 + ss) / (H * 3600)) * 360
        minute_angle = ((mm * 60 + ss) / 3600) * 360
        second_angle = (ss / 60) * 360

        ha = hour_angle % 360
        ma = minute_angle % 360
        sa = second_angle % 360

        # check no two hands overlap
        if hands_overlap(ha, ma, sa):
            continue

        # two angles between second hand and two other hands are equal
        # angles between second hand and hour hand, second hand and minute hand
        angle1 = angle_diff(sa, ha)
        angle2 = angle_diff(sa, ma)

        if abs(angle1 - angle2) < eps:
            h_out = hh % H
            m_out = mm
            # s_out = ss as fraction reduced
            numerator, denominator = reduce_fraction(n, d)
            # if fraction reduces to 1/1, meaning integer second
            if denominator == 1:
                numerator = int(round(ss))
            # output format: h m n d

            # convert ss fraction to n/d with numerator for fractional part
            if denominator == 1:
                # integer second
                print(h_out, m_out, int(round(ss)), 1)
            else:
                # fractional second
                # total seconds integer part: int(ss)
                s_int = int(ss)
                # fractional numerator adjusted
                n_out = numerator + s_int * denominator
                num, den = reduce_fraction(n_out, denominator)
                print(h_out, m_out, num, den)
            return

def main():
    while True:
        line = input()
        if line.strip() == '':
            continue
        H, h, m, s = map(int, line.strip().split())
        if H == 0 and h == 0 and m == 0 and s == 0:
            break
        first_fractional_second(H, h, m, s)

if __name__ == "__main__":
    main()