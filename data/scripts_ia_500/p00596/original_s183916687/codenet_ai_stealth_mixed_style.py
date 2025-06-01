#!/usr/bin/env python3

from collections import deque
import sys

sys.setrecursionlimit(10**7)

def check_graph_connected(E):
    visited = set()
    stack = [next((i for i, edges in enumerate(E) if edges), None)]
    while stack and None not in stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in E[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return all((len(E[i]) == 0 or i in visited) for i in range(len(E)))

def count_odd_degrees(E):
    odd_count = 0
    for edges in E:
        if len(edges) % 2 != 0:
            odd_count += 1
    return odd_count

def main():
    import builtins
    input_func = getattr(builtins, 'input')
    while True:
        try:
            n = input_func()
            if not n:
                break
        except EOFError:
            break
        except:
            break
        A = input_func().split()
        E = [[] for _ in range(7)]
        
        # Adjacency build using map and for comprehension mixture
        list(map(lambda s: (E[int(s[0])].append(int(s[1])), E[int(s[1])].append(int(s[0]))), A))
        
        if count_odd_degrees(E) > 2:
            print("No")
            continue
        
        if check_graph_connected(E):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()