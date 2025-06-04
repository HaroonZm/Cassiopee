running = True
while running:
    n = input()
    if n == 0:
        running = False
        continue

    status = {}
    god_status = -1
    results = {}

    for i in range(n):
        line = raw_input()
        parts = line.split()
        # M, D = map(int, parts[0].split("/"))
        h, m = map(int, parts[1].split(":"))
        minute = h * 60 + m
        is_in = (parts[2] == 'I')
        id_number = parts[3]

        if id_number == '000':
            # goddess handling
            if is_in:
                god_status = minute
            else:
                for k in status:
                    if k != id_number and status[k] != -1:
                        if k not in results:
                            results[k] = 0
                        results[k] = results[k] + (minute - max(god_status, status[k]))
                god_status = -1
        else:
            if is_in:
                status[id_number] = minute
            else:
                if god_status != -1:
                    if id_number not in results:
                        results[id_number] = 0
                    results[id_number] = results[id_number] + (minute - max(god_status, status[id_number]))
                status[id_number] = -1

    if results:
        print max(results.values())
    else:
        print 0