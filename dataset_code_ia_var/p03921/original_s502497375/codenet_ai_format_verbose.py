import sys
import copy
import math
import heapq
import itertools as itertools_module
import fractions
import re
import bisect
import collections as collections_module

class UnionFind:
    def __init__(self, num_elements):
        self.node_ranks = [0] * num_elements
        self.parent_of_node = list(range(num_elements))
        self.num_connected_components = num_elements

    def find_root(self, node):
        if node == self.parent_of_node[node]:
            return node
        self.parent_of_node[node] = self.find_root(self.parent_of_node[node])
        return self.parent_of_node[node]

    def are_in_same_group(self, node1, node2):
        return self.find_root(node1) == self.find_root(node2)

    def union_groups(self, node1, node2):
        root1 = self.find_root(node1)
        root2 = self.find_root(node2)
        if root1 == root2:
            return

        self.num_connected_components -= 1
        if self.node_ranks[root1] > self.node_ranks[root2]:
            self.parent_of_node[root2] = root1
        else:
            self.parent_of_node[root1] = root2
            if self.node_ranks[root1] == self.node_ranks[root2]:
                self.node_ranks[root2] += 1

    def get_num_groups(self):
        return self.num_connected_components

# Read input values for number of people and number of languages
num_people, num_languages = map(int, raw_input().split())

# Read known languages for each person
person_language_lists = [map(int, raw_input().split()) for _ in xrange(num_people)]

# For each language, track the first person encountered who knows it
language_first_person = [-1] * num_languages

union_find = UnionFind(num_people)

for person_index in range(num_people):

    num_languages_known_by_person = person_language_lists[person_index][0]
    
    for language_position in range(1, num_languages_known_by_person + 1):
        current_language = person_language_lists[person_index][language_position] - 1

        if language_first_person[current_language] == -1:
            language_first_person[current_language] = person_index
        else:
            union_find.union_groups(language_first_person[current_language], person_index)

if union_find.get_num_groups() == 1:
    print "YES"
else:
    print "NO"