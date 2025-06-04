import sys

def set_recursion_limit():
    sys.setrecursionlimit(10**9)

def read_values():
    return list(map(int, input().split()))

def create_adjacency_list(n, m):
    return [[] for _ in range(n + m)]

def process_input_lines(n, m, adjacency_list):
    for i in range(n):
        s = read_values()
        process_single_line(i, s, n, adjacency_list)

def process_single_line(person_index, skills, n, adjacency_list):
    for skill in skills[1:]:
        connect_person_and_skill(person_index, skill, n, adjacency_list)

def connect_person_and_skill(person_index, skill, n, adjacency_list):
    skill_index = get_skill_index(skill, n)
    adjacency_list[person_index].append(skill_index)
    adjacency_list[skill_index].append(person_index)

def get_skill_index(skill, n):
    return n + skill - 1

def initialize_visited(size):
    return [False] * size

def dfs_from_zero(n, adjacency_list, visited):
    run_dfs(0, adjacency_list, visited)

def run_dfs(node, adjacency_list, visited):
    mark_visited(node, visited)
    for neighbor in adjacency_list[node]:
        if not is_visited(neighbor, visited):
            run_dfs(neighbor, adjacency_list, visited)

def mark_visited(node, visited):
    visited[node] = True

def is_visited(node, visited):
    return visited[node]

def check_and_print_result(n, visited):
    if are_all_visited(n, visited):
        print_yes()
    else:
        print_no()

def are_all_visited(n, visited):
    for i in range(n):
        if not visited[i]:
            return False
    return True

def print_yes():
    print("YES")

def print_no():
    print("NO")

def main():
    set_recursion_limit()
    n, m = read_values()
    adjacency_list = create_adjacency_list(n, m)
    process_input_lines(n, m, adjacency_list)
    visited = initialize_visited(n + m)
    dfs_from_zero(n, adjacency_list, visited)
    check_and_print_result(n, visited)

main()