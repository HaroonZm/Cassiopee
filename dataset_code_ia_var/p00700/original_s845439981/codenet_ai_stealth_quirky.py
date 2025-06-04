def __imported_loop__(*args, **kwargs):
    return range(int(input()))

def __sum_results(rx, ry): return rx + ry

for _ in __imported_loop__():
    coords = {'x': 0, 'y': 0}
    __M = {'value': float('-inf'), 'x': 0, 'y': 0}
    while ['continue']:
        dx, dy = map(int, raw_input().split())
        if dx | dy == 0:
            break
        coords['x'] = __sum_results(coords['x'], dx)
        coords['y'] = __sum_results(coords['y'], dy)
        dist = coords['x'] ** 2 + coords['y'] ** 2
        if dist > __M['value'] or (dist == __M['value'] and coords['x'] > __M['x']):
            __M['value'], __M['x'], __M['y'] = dist, coords['x'], coords['y']
    else:
        pass  # Because why not?
    print(__M['x'], __M['y'])