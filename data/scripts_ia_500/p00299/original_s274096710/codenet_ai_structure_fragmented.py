import sys
import re
import math
import itertools

def parse_input(file):
    n,c = map(int, file.readline().split())
    p = re.compile('(\d+)(\D+)(\d+)(\D+)(\d+)')
    constraints = [p.match(line).groups() for line in file]
    return n, c, constraints

def to_zero_indexed(value):
    return int(value) - 1

def convert_constraint_to_edge(ai, oi, bi, si, di):
    fr = to_zero_indexed(ai)
    to = to_zero_indexed(bi)
    weight = int(di)
    return fr, oi, to, si, weight

def create_edge(fr, to, weight, si):
    edges = []
    if si == '-':
        edges.append((fr, to, weight if to else 0))
        edges.append((to, fr, 0))
    else:
        edges.append((to, fr, -weight))
    return edges

def handle_oi_star(fr, to, weight, oi, si, floating_edges, fixed_edges):
    if fr != 0 and to != 0:
        floating_edges.append((create_edge(fr,to,weight,si), create_edge(to,fr,weight,si)))
        return True
    if oi == '*':
        oi = '<=' if fr < to else '>='
    if oi == '>=':
        fr, to = to, fr
    fixed_edges.extend(create_edge(fr, to, weight, si))
    return False

def process_constraints(constraints):
    fixed_edges = []
    floating_edges = []
    for ai, oi, bi, si, di in constraints:
        fr, oi, to, si, weight = convert_constraint_to_edge(ai, oi, bi, si, di)
        if oi == '*':
            if handle_oi_star(fr, to, weight, oi, si, floating_edges, fixed_edges):
                continue
        elif oi == '>=':
            fr, to = to, fr
            fixed_edges.extend(create_edge(fr, to, weight, si))
        else:
            fixed_edges.extend(create_edge(fr, to, weight, si))
    return fixed_edges, floating_edges

def initialize_distance(length):
    distance = [float('inf')] * length
    distance[0] = 0
    return distance

def relax_edges(distance, edges):
    for fr, to, weight in edges:
        if distance[to] > distance[fr] + weight:
            distance[to] = distance[fr] + weight

def has_negative_cycle(distance, edges):
    for fr, to, weight in edges:
        if distance[to] > distance[fr] + weight:
            return True
    return False

def verify_no_negative_min_distance(distance):
    return min(distance[1:]) < 0

def bellmanford(edges, length):
    distance = initialize_distance(length)
    for _ in range(length):
        relax_edges(distance, edges)
    if has_negative_cycle(distance, edges):
        return -1
    if verify_no_negative_min_distance(distance):
        return -1
    return max(distance)

def calculate_distances(n, fixed_edges, floating_edges):
    distance = []
    for edges in itertools.product(*floating_edges):
        combined_edges = fixed_edges + [y for x in edges for y in x]
        distance.append(bellmanford(combined_edges, n))
    return distance

def main():
    f = sys.stdin
    n, c, constraints = parse_input(f)
    fixed_edges, floating_edges = process_constraints(constraints)
    distance = calculate_distances(n, fixed_edges, floating_edges)
    print(max(distance))

main()