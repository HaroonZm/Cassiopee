for iteration_index in xrange(input()):
    outs_count, bases_occupied, points_scored = 0, 0, 0
    while outs_count < 3:
        event_input = raw_input()
        if event_input == "OUT":
            outs_count += 1
        if event_input == "HIT":
            bases_occupied += 1
        if event_input == "HOMERUN":
            points_scored += bases_occupied + 1
            bases_occupied = 0
    if bases_occupied >= 4:
        points_scored += bases_occupied - 3
    print points_scored