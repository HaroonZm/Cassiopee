# Définition d'une constante représentant l'infini
INFINITY = 10 ** 9

while True:

    number_of_events_input = input()

    if not number_of_events_input:
        break

    number_of_events = int(number_of_events_input)

    minimum_distances = [INFINITY] * 4
    minimum_distances[0] = 0

    current_position = 0
    current_time = 0

    failure_event_index = -1

    positions = []
    times = []

    for event_index in xrange(number_of_events):
        position, timestamp = map(int, raw_input().split())
        positions.append(position)
        times.append(timestamp)

    for event_index in xrange(number_of_events):

        target_position = positions[event_index]
        target_time = times[event_index]

        distance_to_target = abs(target_position - current_position)
        is_move_possible = False
        min_possible_distance = INFINITY

        for jumps_used in xrange(3, -1, -1):

            if jumps_used < 3:
                minimum_distances[jumps_used + 1] = INFINITY

            if minimum_distances[jumps_used] == INFINITY:
                continue

            # Tentative de mouvement direct
            if jumps_used < 3 and distance_to_target * (jumps_used + 1) <= target_time - current_time:
                is_move_possible = True
                minimum_distances[jumps_used + 1] = minimum_distances[jumps_used] + distance_to_target

            # Tentative via retour au point de départ
            if current_position * (jumps_used + 1) + target_position <= target_time - current_time:
                min_possible_distance = min(min_possible_distance, minimum_distances[jumps_used] + current_position + target_position)
                is_move_possible = True

        minimum_distances[1] = min_possible_distance
        minimum_distances[0] = INFINITY

        if not is_move_possible:
            failure_event_index = event_index + 1
            break

        current_position = target_position
        current_time = target_time

    if failure_event_index != -1:
        print "NG", failure_event_index
        continue

    print "OK", (min(minimum_distances[1:]) + target_position)