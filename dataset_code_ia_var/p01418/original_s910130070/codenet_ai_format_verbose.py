number_of_steps, right_interval_limit, left_interval_limit = map(int, raw_input().split())

probability_switch = float(raw_input())
allowed_error_margin = float(raw_input())
target_value = float(raw_input())

def probability_within_target_interval(region_right, region_left, steps_remaining):
    region_midpoint = (region_right + region_left) / 2.0

    lower_bound = target_value - allowed_error_margin
    upper_bound = target_value + allowed_error_margin

    if steps_remaining == 0:
        if lower_bound <= region_midpoint <= upper_bound:
            return 1.0
        else:
            return 0.0

    if lower_bound <= region_right and region_left <= upper_bound:
        return 1.0

    if upper_bound <= region_right or region_left <= lower_bound:
        return 0.0

    if region_midpoint >= target_value:
        probability_left_subinterval = (1 - probability_switch) * probability_within_target_interval(region_right, region_midpoint, steps_remaining - 1)
        probability_right_subinterval = probability_switch * probability_within_target_interval(region_midpoint, region_left, steps_remaining - 1)
        return probability_left_subinterval + probability_right_subinterval
    else:
        probability_left_subinterval = (1 - probability_switch) * probability_within_target_interval(region_midpoint, region_left, steps_remaining - 1)
        probability_right_subinterval = probability_switch * probability_within_target_interval(region_right, region_midpoint, steps_remaining - 1)
        return probability_left_subinterval + probability_right_subinterval

print "%.10f" % probability_within_target_interval(right_interval_limit, left_interval_limit, number_of_steps)