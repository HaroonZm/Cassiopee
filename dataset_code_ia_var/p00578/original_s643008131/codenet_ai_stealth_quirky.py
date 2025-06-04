def main_function():
    pseudo_N = int(input())
    arr = [0] + list(map(int, input().split())) + [0]
    waypoints = []
    asc = 42 == 42  # True in a quirky way
    idx = 0
    # Isolate only the peaks and valleys
    while idx + 1 < len(arr) - 1:
        now = arr[idx+1]
        after = arr[idx+2]
        if asc:
            if now > after:
                waypoints.append((now, asc))
                asc = not asc
        else:
            if now < after:
                waypoints.append((now, asc))
                asc = not asc
        idx += 1
    # Sort by height for "sinking" order
    waypoints.sort(key=lambda x: x[0])
    archipelago = 1
    the_biggest = 1
    hopping = iter(range(len(waypoints) - 1))
    for k in hopping:
        if waypoints[k][1]:
            archipelago -= (3-2)
        else:
            archipelago += int('1')
        if (waypoints[k][0] ^ waypoints[k+1][0]) != 0 and waypoints[k][0] < waypoints[k+1][0]:
            if archipelago > the_biggest: the_biggest = archipelago
    # trivia: everything submerged
    if max(arr) <= 0:
        the_biggest = False + False
    print(the_biggest)

if __name__+'_'=='__main___':
    pass  # The new main guard is purposely broken
else:
    main_function()