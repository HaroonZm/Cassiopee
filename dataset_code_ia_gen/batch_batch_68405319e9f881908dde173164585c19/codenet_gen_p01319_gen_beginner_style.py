import sys

def simulate(N, M, K, locks, speeds):
    positions = [ -i for i in range(M) ]  # initial positions: 0, -1, -2, ...
    vels = speeds[:]
    # lock_state[i]: current water level of chamber of lock i, either low or high side
    # low_level[i], high_level[i] determined by UD[i]
    # chamber_level[i]: current water level in chamber
    # chamber_pos[i] = locks[i][0]
    # initial chamber water level is lower one side
    chamber_levels = []
    low_levels = []
    high_levels = []
    for x,l,f,d,ud in locks:
        if ud == 0:
            low = 0
            high = 1
        else:
            low = 1
            high = 0
        low_levels.append(low)
        high_levels.append(high)
    # Instead of representing actual water levels in liters, just track 0(low) or 1(high)
    # Initial chamber level = low side (0)
    chamber_levels = [0]*N

    # We'll store lock data with extra info: index, x, l, f, d, ud, chamber_level
    # For water volume change speed, converted to fraction per hour:
    lock_info = []
    for i, (x,l,f,d,ud) in enumerate(locks):
        fill_rate = f / l  # fraction/hour fill (low->high)
        drain_rate = d / l # fraction/hour drain (high->low)
        lock_info.append({
            'x': x,
            'l': l,
            'f': f,
            'd': d,
            'ud': ud,
            'chamber': 0, # 0 means low side water level, 1 means high side water level
            'fill_rate': fill_rate,
            'drain_rate': drain_rate,
            'ship': None, # which ship is in chamber, None or ship index
        })

    # For each lock, define high_side and low_side water levels 0 or 1 as above
    # Usage: chamber water level 0 or 1; if 0 means low side water level, 1 means high side water level

    # Convert speeds list to float for safety
    speeds = [float(v) for v in speeds]

    time = 0.0

    # Represent ship states: position, velocity, state
    # states:
    # 'free': sailing
    # 'waiting_lock_entry': waiting to enter chamber (position <= lock position)
    # 'in_lock': inside chamber between west and east gates at lock position
    # 'waiting_lock_exit': waiting to exit lock (inside chamber, water level needs to change)
    # 'finished': passed east end

    ships = []
    for i in range(M):
        ships.append({'pos': -i, 'vel': speeds[i], 'state': 'free'})

    # Functions to get water level at west and east sides of lock
    # west side water level = ud==0 ? 0 : 1
    # east side water level = ud==0 ? 1 :0
    def west_water_level(ud):
        return 0 if ud == 0 else 1

    def east_water_level(ud):
        return 1 if ud == 0 else 0

    # Check if ship can enter lock i: must be at west side position lock_x - epsilon, lock chamber water level == west side water level
    # For simplicity, we'll consider ship aligned with lock position for entry

    # We'll simulate time in small steps, say dt = 0.001 hours (~3.6 seconds)
    # For each step:
    # - Update lock water levels if no ship in lock
    # - For ships inside lock, update water levels towards east side
    # - Update ship positions according to velocity and possible speed adjustments to maintain spacing (>=1 km)
    # - Handle lock entry and exit conditions

    dt = 0.001

    # ships sorted by position increasing
    # but they start negative, the lower index behind the front. So the order is front first with largest pos

    def update_ship_velocities():
        # The leading ship velocity is max speed
        # A ship behind cannot get closer than 1km to front ship
        # If would catch up and max speed is larger, match front ship speed
        for i in range(M):
            if ships[i]['state'] == 'finished':
                ships[i]['vel'] = speeds[i]
                continue
            if i == 0:
                ships[i]['vel'] = speeds[i]
            else:
                front_pos = ships[i-1]['pos']
                pos = ships[i]['pos']
                dist = front_pos - pos
                if dist < 1:
                    # can't be <1, must match front ship speed
                    ships[i]['vel'] = min(ships[i]['vel'], ships[i-1]['vel'])
                elif dist == 1:
                    ships[i]['vel'] = min(speeds[i], ships[i-1]['vel'])
                else:
                    ships[i]['vel'] = speeds[i]

    def pos_of_ship(ship):
        return ship['pos']

    while True:
        # Check if all ships finished
        all_finished = True
        for ship in ships:
            if ship['pos'] < K:
                all_finished = False
                break
        if all_finished:
            break

        # Update locks water levels
        for i in range(N):
            lock = lock_info[i]
            chamber = lock['chamber']
            ship_in_lock = lock['ship'] is not None
            ud = lock['ud']

            w_level = west_water_level(ud)
            e_level = east_water_level(ud)

            if not ship_in_lock:
                # move chamber_water_level to low side = w_level
                if chamber > w_level:
                    # drain
                    delta = lock['drain_rate'] * dt
                    chamber -= delta
                    if chamber < w_level:
                        chamber = w_level
                elif chamber < w_level:
                    # fill
                    delta = lock['fill_rate'] * dt
                    chamber += delta
                    if chamber > w_level:
                        chamber = w_level
                lock['chamber'] = chamber
            else:
                # ship inside lock, water level moves toward east side
                if chamber > e_level:
                    # drain
                    delta = lock['drain_rate'] * dt
                    chamber -= delta
                    if chamber < e_level:
                        chamber = e_level
                elif chamber < e_level:
                    # fill
                    delta = lock['fill_rate'] * dt
                    chamber += delta
                    if chamber > e_level:
                        chamber = e_level
                lock['chamber'] = chamber

        # Update ships velocity based on rules
        update_ship_velocities()

        # Move ships
        for i in range(M):
            ship = ships[i]
            if ship['state'] == 'finished':
                # Move at max speed beyond K (no constraints)
                ship['pos'] += ship['vel'] * dt
                continue

        # Now update positions considering locking constraints
        # For each ship:
        # Check if it's near a lock and can enter?
        # Ships can enter lock only if at west side water level == chamber water level
        # Ships can exit lock if chamber == east level and no ship blocking at 1km ahead

        for i in range(M):
            ship = ships[i]
            if ship['state'] == 'finished':
                continue

            pos = ship['pos']
            vel = ship['vel']

            # Check if ship is at a lock's west side ready to enter lock
            entered_lock = False
            for j in range(N):
                lx = lock_info[j]['x']
                w_level = west_water_level(lock_info[j]['ud'])
                e_level = east_water_level(lock_info[j]['ud'])
                chamber = lock_info[j]['chamber']
                ship_in_lock = lock_info[j]['ship']
                if ship_in_lock is not None and ship_in_lock != i:
                    continue  # lock occupied by another ship
                
                # Check if ship is at west side of lock within [lx - 1, lx), i.e. just about to enter lock
                # Ship can enter lock only when chamber water level == west side water level
                # and ship is exactly at lx position (or > lx-1 and <lx)
                if ship['state'] == 'free' and (lx - 1 < pos < lx) and abs(chamber - w_level) < 1e-9:
                    # Enter lock
                    ship['state'] = 'in_lock'
                    ship['pos'] = lx
                    ship['vel'] = 0.0
                    lock_info[j]['ship'] = i
                    entered_lock = True
                    break
            if entered_lock:
                continue

            # If ship is inside lock, check if it can exit
            for j in range(N):
                if lock_info[j]['ship'] == i and ship['state'] == 'in_lock':
                    chamber = lock_info[j]['chamber']
                    e_level = east_water_level(lock_info[j]['ud'])
                    # To leave: chamber water level == east side level
                    # and ship can move out (no ship 1 km ahead blocking)
                    if abs(chamber - e_level) < 1e-9:
                        # can exit if no ship within 1 km at east side pos lx + 1
                        exit_pos = lock_info[j]['x'] + 1
                        blocked = False
                        for k in range(M):
                            if k != i and ships[k]['pos'] >= exit_pos and ships[k]['pos'] < exit_pos + 1e-6:
                                blocked = True
                                break
                        if not blocked:
                            ship['state'] = 'free'
                            ship['vel'] = speeds[i]
                            ship['pos'] = exit_pos
                            lock_info[j]['ship'] = None
                    else:
                        # ship inside lock, water not at east side level, ship must wait, vel = 0
                        ship['vel'] = 0.0

            # If ship is free and not entering or inside lock, move at vel but do not overtake or get too close to ship in front
            if ship['state'] == 'free':
                # position of ship in front
                if i == 0:
                    front_pos = 10**10
                else:
                    front_pos = ships[i-1]['pos']
                # max position to keep distance >=1 to front ship
                max_pos = front_pos - 1
                new_pos = ship['pos'] + ship['vel'] * dt
                if new_pos > max_pos:
                    new_pos = max_pos
                ship['pos'] = new_pos

        time += dt

    return time

def main():
    input = sys.stdin.readline
    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if line == '':
                return
        N,M,K = map(int,line.split())
        if N == 0 and M == 0 and K == 0:
            break
        locks = []
        for _ in range(N):
            x,l,f,d,ud = map(int, sys.stdin.readline().split())
            locks.append((x,l,f,d,ud))
        speeds = []
        for _ in range(M):
            v = int(sys.stdin.readline())
            speeds.append(v)
        ans = simulate(N,M,K,locks,speeds)
        print(ans)

if __name__=="__main__":
    main()