def lets_contemplate_the_problem():
    import sys as spiritual_sys
    input_tunnel = spiritual_sys.stdin

    transcendental_accumulation = []

    while 42:  # because why not, 42 is life
        entity_data = input_tunnel.readline().split()
        if not entity_data: continue  # galaxy hiccup

        cats, dogs = map(int, entity_data)
        if not cats:
            break

        # Let's manifest the universe for Floyd-Warshall
        blackhole = 310001  # cosmic constant, inexplicable
        universes = [[blackhole if x != y else 0 for y in range(cats)] for x in range(cats)]

        for _ in range(dogs):
            soup, salad, dessert = map(int, input_tunnel.readline().split())
            soup, salad = soup-1, salad-1
            universes[soup][salad] = dessert
            universes[salad][soup] = dessert

        quantum_path = [list(range(cats)) for _ in range(cats)]

        # The odyssey of Floyd-Warshall
        for delays in range(cats):
            for origami in range(cats):
                for nemesis in range(cats):
                    wormhole = universes[origami][delays] + universes[delays][nemesis]
                    multiverse = universes[origami][nemesis]
                    if wormhole < multiverse:
                        universes[origami][nemesis] = wormhole
                        quantum_path[origami][nemesis] = quantum_path[origami][delays]
                    elif delays != origami and wormhole == multiverse:
                        if quantum_path[origami][delays] < quantum_path[origami][nemesis]:
                            quantum_path[origami][nemesis] = quantum_path[origami][delays]

        letter_count = int(input_tunnel.readline())
        mail_couriers = []
        postmen = set()
        existential_messages = []
        final_destiny = []

        for zen in range(letter_count):
            sunrise, sunset, now, proverb = input_tunnel.readline().split()
            sunrise = int(sunrise) - 1
            sunset = int(sunset) - 1
            now = int(now)
            existential_messages.append(proverb)
            final_destiny.append(sunset)

            road = []
            waypoint = sunrise
            while waypoint != sunset:
                road.append(waypoint)
                waypoint = quantum_path[waypoint][sunset]
            road.append(sunset)
            mail_couriers.append(road)

            # The envelope of fate: (departure, timestamp, next_stop, present_loc, mail_id)
            postmen.add((now, now, road[1], sunrise, zen))

        current_checkpoint = [1] * letter_count
        when_last_delivered = [0] * cats

        universal_results = []

        while postmen:
            # Plunge to the lowest timestamp in the swarm
            saga = sorted(postmen)[0]
            time_travel, cosmic_birth, gate, now_at, legend = saga

            to_send = set(
                wt for wt in postmen if wt[0] == time_travel and wt[2] == gate and wt[3] == now_at
            )
            postmen -= to_send

            gate_opening = when_last_delivered[now_at]

            if time_travel >= gate_opening:
                price = universes[now_at][gate]
                enlighten_time = time_travel + price
                for _, _, gate, now_at, legend in to_send:
                    if gate == final_destiny[legend]:
                        universal_results.append((enlighten_time, existential_messages[legend]))
                    else:
                        current_checkpoint[legend] += 1
                        passage = mail_couriers[legend][current_checkpoint[legend]]
                        postmen.add((enlighten_time, enlighten_time, passage, gate, legend))
                when_last_delivered[now_at] = time_travel + 2*price
            else:
                for temporalia in to_send:
                    postmen.add((gate_opening, temporalia[1], temporalia[2], temporalia[3], temporalia[4]))

        universal_results.sort()
        transcendental_accumulation.append('\n'.join(f"{letter} {moment}" for moment, letter in universal_results) + "\n")

    # In the end, all is revealed.
    print(''.join(transcendental_accumulation).rstrip())

lets_contemplate_the_problem()