def get_next_input():
    return input()

def parse_input_line():
    line = raw_input()
    return line.split(":")

def extract_group_and_members(parsed_line):
    g = parsed_line[0]
    m = parsed_line[1][:-1].split(",")
    return g, m

def append_group(gs, g):
    gs.append(g)

def append_members(ms, m):
    ms.append(m)

def initialize_dg(dg, g):
    dg[g] = []

def create_group_data_structures(n):
    gs = []
    ms = []
    dg = {}
    for i in xrange(n):
        parsed_line = parse_input_line()
        g, m = extract_group_and_members(parsed_line)
        append_group(gs, g)
        append_members(ms, m)
        initialize_dg(dg, g)
    return gs, ms, dg

def member_in_dg(me, i, dg):
    return me[i] in dg

def get_index(gs, member):
    return gs.index(member)

def ensure_not_in_group(dg, group, e):
    if e not in dg[group]:
        dg[group].append(e)

def traverse_and_update(dg, gs, ms, used, v):
    if used[v]:
        return dg[gs[v]]
    used[v] = 1
    me = ms[v]
    for i in xrange(len(me)):
        if member_in_dg(me, i, dg):
            idx = get_index(gs, me[i])
            ret = traverse_and_update(dg, gs, ms, used, idx)
            process_ret_elements(ret, dg, gs, v)
        else:
            ensure_not_in_group(dg, gs[v], me[i])
    return dg[gs[v]]

def process_ret_elements(ret, dg, gs, v):
    for e in ret:
        ensure_not_in_group(dg, gs[v], e)

def start_dfs(dg, gs, ms, n):
    used = [0]*n
    traverse_and_update(dg, gs, ms, used, 0)

def main():
    while True:
        n = get_next_input()
        if not n:
            break
        n = int(n)
        gs, ms, dg = create_group_data_structures(n)
        start_dfs(dg, gs, ms, n)
        print len(dg[gs[0]])

main()