def is_leap_year(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

def next_birthday(y, m, d, current_year):
    # Returns the datetime date of the birthday in current_year
    # Adjusts Feb 29 to Mar 1 if current_year is non-leap
    if m == 2 and d == 29:
        if is_leap_year(current_year):
            return (current_year, 2, 29)
        else:
            return (current_year, 3, 1)
    else:
        return (current_year, m, d)

def age_at(y_birth, m_birth, d_birth, y, m, d):
    # Calculate age at date (y,m,d)
    age = y - y_birth
    b_y, b_m, b_d = y_birth, m_birth, d_birth
    # Adjust birth date if Feb 29
    if m_birth == 2 and d_birth == 29 and not is_leap_year(y):
        b_m, b_d = 3, 1

    if (m, d) < (b_m, b_d):
        age -= 1
    return age

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

# The max age difference will be a stable max taken from the difference in ages at a birthday boundary
# Check the difference on every birthday (for each person) from max(y1,y2) to max(y1,y2)+3000 (safe max span)
# Note: age difference changes only right after a birthday passes for one of them

start_year = min(y1, y2)
end_year = max(y1, y2) + 3000

max_diff = abs((y2 - y1))  # minimal guess, difference at birth

for year in range(start_year, end_year + 1):

    # birthdays of person 1 and person 2 in this year
    b1 = next_birthday(y1, m1, d1, year)
    b2 = next_birthday(y2, m2, d2, year)

    # check age difference just before and just after each birthday, because difference changes when someone ages up

    # dates to check:
    # just before b1 birthday (e.g day before)
    if b1[2] > 1:
        check1 = (year, b1[1], b1[2] - 1)
    else:
        # day=1 => day before is last day of previous month
        m_prev = b1[1] - 1
        y_prev = year
        if m_prev == 0:
            m_prev = 12
            y_prev -= 1
        # Get last day of m_prev in y_prev
        if m_prev == 2:
            ld = 29 if is_leap_year(y_prev) else 28
        elif m_prev in [4,6,9,11]:
            ld = 30
        else:
            ld = 31
        check1 = (y_prev, m_prev, ld)

    # just after b1 birthday (exact birthday date)
    check2 = b1

    # just before b2 birthday
    if b2[2] > 1:
        check3 = (year, b2[1], b2[2] - 1)
    else:
        m_prev = b2[1] - 1
        y_prev = year
        if m_prev == 0:
            m_prev = 12
            y_prev -= 1
        if m_prev == 2:
            ld = 29 if is_leap_year(y_prev) else 28
        elif m_prev in [4,6,9,11]:
            ld = 30
        else:
            ld = 31
        check3 = (y_prev, m_prev, ld)

    # just after b2 birthday
    check4 = b2

    candidates = [check1, check2, check3, check4]
    for (yy, mm, dd) in candidates:
        # Only check valid dates inside sensible range (birth years inclusive)
        if yy < y1 and yy < y2:
            continue
        if yy < y1 or yy < y2:
            # not both born yet, but fine to check
            pass
        a1 = age_at(y1, m1, d1, yy, mm, dd)
        a2 = age_at(y2, m2, d2, yy, mm, dd)
        diff = abs(a1 - a2)
        if diff > max_diff:
            max_diff = diff

print(max_diff)