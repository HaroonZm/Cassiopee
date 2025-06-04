def parse_time_to_minutes(time_str):
    """
    Convert a time string 'hh:mm' in 24-hour format to total minutes
    from midnight (0:00).
    """
    hh, mm = map(int, time_str.split(':'))
    return hh * 60 + mm

def is_in_range(minute, start, end):
    """
    Check if a time in minutes is within the range [start,end].
    This function supports ranges that can wrap over midnight.
    """
    if start <= end:
        return start <= minute <= end
    else:
        # For ranges passing midnight, e.g., 21:00 ~ 01:59
        return minute >= start or minute <= end

def truncate_ratio(ok, total):
    """
    Compute the integer percentage truncated (not rounded).
    """
    return (ok * 100) // total

def main():
    """
    Main logic to process input datasets and compute ok check ratios
    for lunch, dinner, and midnight times.
    """
    # Define time ranges in minutes from midnight (0:00)
    # Lunch: 11:00 ~ 14:59
    lunch_start = 11 * 60
    lunch_end = 14 * 60 + 59

    # Dinner: 18:00 ~ 20:59
    dinner_start = 18 * 60
    dinner_end = 20 * 60 + 59

    # Midnight: 21:00 ~ 01:59 (wraps over midnight)
    midnight_start = 21 * 60
    midnight_end = 1 * 60 + 59

    while True:
        n_line = input().strip()
        if n_line == '0':
            # End of all datasets
            break
        n = int(n_line)

        # Counters for each time range: (ok_checks, total_checks)
        lunch_ok = 0
        lunch_total = 0
        dinner_ok = 0
        dinner_total = 0
        midnight_ok = 0
        midnight_total = 0

        for _ in range(n):
            line = input().strip()
            time_str, mm_str = line.split()
            provide_time = parse_time_to_minutes(time_str)
            provided_mm = int(mm_str)

            # Categorize the check by print time
            if is_in_range(provide_time, lunch_start, lunch_end):
                # It's lunch
                lunch_total += 1
                if provided_mm <= 8:
                    lunch_ok += 1
            elif is_in_range(provide_time, dinner_start, dinner_end):
                # Dinner time
                dinner_total += 1
                if provided_mm <= 8:
                    dinner_ok += 1
            elif is_in_range(provide_time, midnight_start, midnight_end):
                # Midnight time
                midnight_total += 1
                if provided_mm <= 8:
                    midnight_ok += 1
            else:
                # Out of any range: ignore this check
                pass

        # Print results for lunch
        print("lunch", (truncate_ratio(lunch_ok, lunch_total)
                       if lunch_total > 0 else "no guest"))
        # Print results for dinner
        print("dinner", (truncate_ratio(dinner_ok, dinner_total)
                        if dinner_total > 0 else "no guest"))
        # Print results for midnight
        print("midnight", (truncate_ratio(midnight_ok, midnight_total)
                          if midnight_total > 0 else "no guest"))


if __name__ == "__main__":
    main()