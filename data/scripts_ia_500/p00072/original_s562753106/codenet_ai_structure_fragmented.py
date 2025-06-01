#!/usr/bin/env python

"""参考文献
http://ja.wikipedia.org/wiki/クラスカル法
"""
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sys import stdin

def read_num_node():
    return int(stdin.readline())

def should_stop(num_node):
    return not num_node

def read_num_edges():
    return int(stdin.readline())

def read_edge():
    line = stdin.readline()
    return parse_edge(line)

def parse_edge(line):
    parts = line.split(',')
    return [int(part) for part in parts]

def read_all_edges(num_edges):
    edges = []
    i = 0
    while i < num_edges:
        edges.append(read_edge())
        i += 1
    return edges

def sort_edges(edges):
    def key_func(edge):
        n1, n2, d = edge
        return d
    edges.sort(key=key_func, reverse=True)

def initialize_forest(num_node):
    forest = set()
    i = 0
    while i < num_node:
        forest.add(frozenset([i]))
        i += 1
    return forest

def pop_edge(edges):
    return edges.pop()

def find_trees_for_nodes(forest, node1, node2):
    a = None
    b = None
    for tree in forest:
        if node1 in tree:
            a = tree
        if node2 in tree:
            b = tree
        if a and b:
            break
    return a, b

def union_forest(forest, a, b):
    union_set = a | b
    forest.add(union_set)
    forest.remove(a)
    forest.remove(b)

def process_edges(forest, edges):
    spanning = []
    while edges:
        node1, node2, distance = pop_edge(edges)
        a, b = find_trees_for_nodes(forest, node1, node2)
        if a != b:
            union_forest(forest, a, b)
            spanning.append(distance)
    return spanning

def calculate_result(spanning):
    total = 0
    for distance in spanning:
        total += (distance // 100) - 1
    return total

def main_loop():
    while True:
        num_node = read_num_node()
        if should_stop(num_node):
            break
        
        num_edges = read_num_edges()
        edges = read_all_edges(num_edges)
        sort_edges(edges)
        forest = initialize_forest(num_node)
        spanning = process_edges(forest, edges)
        result = calculate_result(spanning)
        print(result)

if __name__ == '__main__':
    main_loop()