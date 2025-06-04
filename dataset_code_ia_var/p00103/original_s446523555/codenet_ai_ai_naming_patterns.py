for game_index in xrange(input()):
    out_count = 0
    base_stack = 0
    point_total = 0
    while out_count < 3:
        event_input = raw_input()
        if event_input == "OUT":
            out_count += 1
        if event_input == "HIT":
            base_stack += 1
        if event_input == "HOMERUN":
            point_total += base_stack + 1
            base_stack = 0
    if base_stack >= 4:
        point_total += base_stack - 3
    print point_total