###############################################################################

from bisect import bisect_left as binl

def intin():
    input_tuple = input().split()
    if len(input_tuple) <= 1:
        return int(input_tuple[0])
    return tuple(map(int, input_tuple))

def intina():
    return [int(i) for i in input().split()]

def intinl(count):
    return [intin() for _ in range(count)]

def modadd(x, y):
    global mod
    return (x + y) % mod

def modmlt(x, y):
    global mod
    return (x * sy) % mod

def lcm(x, y):
    while y != 0:
        z = x % y
        x = y
        y = z
    return x

def make_linklist(xylist):
    linklist = {}
    for a, b in xylist:
        linklist.setdefault(a, [])
        linklist.setdefault(b, [])
        linklist[a].append(b)
        linklist[b].append(a)
    return linklist

def calc_longest_distance(linklist, v=1):
    distance_list = {}
    distance_count = 0
    distance = 0
    vlist_previous = []
    vlist = [v]
    nodecount = len(linklist)

    while distance_count < nodecount:
        vlist_next = []
        for v in vlist:
            distance_list[v] = distance
            distance_count += 1
            vlist_next.extend(linklist[v])
        distance += 1
        vlist_to_del = vlist_previous
        vlist_previous = vlist
        vlist = list(set(vlist_next) - set(vlist_to_del))

    max_distance = -1
    max_v = None
    for v, distance in distance_list.items():
        if distance > max_distance:
            max_distance = distance
            max_v = v

    return (max_distance, max_v)

def calc_tree_diameter(linklist, v=1):
    _, u = calc_longest_distance(linklist, v)
    distance, _ = calc_longest_distance(linklist, u)
    return distance

###############################################################################

def main():
    n = intin()
    ablist = intinl(n-1)

    linklist = make_linklist(ablist)
    diameter = calc_tree_diameter(linklist)

    if diameter % 3 == 1:
        print('Second')
    else:
        print('First')

if __name__ == '__main__':
    main()