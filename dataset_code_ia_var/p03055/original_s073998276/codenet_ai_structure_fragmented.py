from bisect import bisect_left as binl

def read_input():
    return input()

def split_input(s):
    return s.split()

def convert_to_int_list(str_list):
    return [int(i) for i in str_list]

def tuple_or_int(lst):
    if len(lst) <= 1:
        return int(lst[0])
    return tuple(map(int, lst))

def intin():
    input_str = read_input()
    input_split = split_input(input_str)
    return tuple_or_int(input_split)

def intina():
    input_str = read_input()
    input_split = split_input(input_str)
    return convert_to_int_list(input_split)

def intinl(count):
    return [intin() for _ in range(count)]

def get_mod():
    global mod
    return mod

def modadd(x, y):
    m = get_mod()
    return (x + y) % m

def modmlt_product(x, y):
    return x * y

def modmlt_modulo(prod):
    global mod
    return prod % mod

def modmlt(x, y):
    prod = modmlt_product(x, y)
    return modmlt_modulo(prod)

def lcm_gcd_inner(x, y):
    while y != 0:
        z = x % y
        x, y = y, z
    return x

def lcm(x, y):
    return lcm_gcd_inner(x, y)

def empty_linklist():
    return {}

def linklist_setdefault(linklist, key):
    linklist.setdefault(key, [])

def linklist_append(linklist, a, b):
    linklist[a].append(b)

def linklist_add(linklist, a, b):
    linklist_setdefault(linklist, a)
    linklist_setdefault(linklist, b)
    linklist_append(linklist, a, b)
    linklist_append(linklist, b, a)

def make_linklist(xylist):
    linklist = empty_linklist()
    for a, b in xylist:
        linklist_add(linklist, a, b)
    return linklist

def calc_init_linklist_vars():
    return {}, 0, 0, [], []

def get_linklist_nodecount(linklist):
    return len(linklist)

def update_vlist_next(linklist, v, vlist_next):
    vlist_next.extend(linklist[v])

def set_distance(distance_list, v, distance):
    distance_list[v] = distance

def increase_distance_count(distance_count):
    return distance_count + 1

def set_vlist_state(vlist_previous, vlist, vlist_next):
    return vlist, list(set(vlist_next) - set(vlist_previous))

def calc_loop(
    linklist, distance_list, distance_count, distance, vlist_previous, vlist, nodecount
):
    while distance_count < nodecount:
        vlist_next = []
        for v in vlist:
            set_distance(distance_list, v, distance)
            distance_count += 1
            update_vlist_next(linklist, v, vlist_next)
        distance += 1
        vlist_to_del = vlist_previous
        vlist_previous, vlist = set_vlist_state(vlist_previous, vlist, vlist_next)
    return distance_list

def find_max_distance(distance_list):
    max_distance = -1
    max_v = None
    for v, d in distance_list.items():
        if d > max_distance:
            max_distance = d
            max_v = v
    return max_distance, max_v

def calc_longest_distance(linklist, v=1):
    distance_list, distance_count, distance, vlist_previous, vlist = calc_init_linklist_vars()
    vlist = [v]
    nodecount = get_linklist_nodecount(linklist)
    while distance_count < nodecount:
        vlist_next = []
        for p in vlist:
            set_distance(distance_list, p, distance)
            distance_count += 1
            update_vlist_next(linklist, p, vlist_next)
        distance += 1
        vlist_to_del = vlist_previous
        vlist_previous = vlist
        vlist = list(set(vlist_next) - set(vlist_to_del))
    return find_max_distance(distance_list)

def calc_tree_diameter_get_u(linklist, v):
    _, u = calc_longest_distance(linklist, v)
    return u

def calc_tree_diameter_get_distance(linklist, u):
    distance, _ = calc_longest_distance(linklist, u)
    return distance

def calc_tree_diameter(linklist, v=1):
    u = calc_tree_diameter_get_u(linklist, v)
    distance = calc_tree_diameter_get_distance(linklist, u)
    return distance

def decide_winner(diameter):
    if diameter % 3 == 1:
        return 'Second'
    else:
        return 'First'

def main_get_n():
    return intin()

def main_get_ablist(n):
    return intinl(n-1)

def main_make_linklist(ablist):
    return make_linklist(ablist)

def main_calc_diameter(linklist):
    return calc_tree_diameter(linklist)

def main_print_winner(diameter):
    print(decide_winner(diameter))

def main():
    n = main_get_n()
    ablist = main_get_ablist(n)
    linklist = main_make_linklist(ablist)
    diameter = main_calc_diameter(linklist)
    main_print_winner(diameter)

if __name__ == '__main__':
    main()