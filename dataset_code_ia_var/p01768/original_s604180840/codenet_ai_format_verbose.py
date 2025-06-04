import sys
from collections import defaultdict, deque

def find_root(element):
    if parent[element] == element:
        return element
    parent[element] = find_root(parent[element])
    return parent[element]

def union_sets(element1, element2):
    root1 = find_root(element1)
    root2 = find_root(element2)
    if rank[root1] < rank[root2]:
        parent[root1] = root2
    else:
        parent[root2] = root1
        if rank[root1] == rank[root2]:
            rank[root1] += 1

element_value = defaultdict(int)
parent = defaultdict(int)
rank = defaultdict(int)

number_of_elements = int(sys.stdin.readline())
for _ in range(number_of_elements):
    element_name, value_str = sys.stdin.readline().split()
    element_value[element_name] = int(value_str)
    parent[element_name] = element_name
    rank[element_name] = 0

number_of_unions = int(sys.stdin.readline())
for _ in range(number_of_unions):
    first_element, second_element = sys.stdin.readline().split()
    if find_root(first_element) != find_root(second_element):
        union_sets(first_element, second_element)

total_minimum_sum = 0
for element in element_value.keys():
    root_element = find_root(element)
    current_root = parent[element]
    element_value[current_root] = min(element_value[current_root], element_value[element])

for element in element_value.keys():
    total_minimum_sum += element_value[find_root(element)]

print(total_minimum_sum)