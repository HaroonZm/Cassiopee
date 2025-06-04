from collections import deque

def power_cache_func_factory():
    power_cache = {}
    def power_with_cache(exp):
        if exp not in power_cache:
            power_cache[exp] = pow(2, exp, MODULO_VAL)
        return power_cache[exp]
    return power_with_cache

MODULO_VAL = 10**9 + 7
node_count = int(input())
parent_list = list(map(int, input().split()))
child_sets = [set() for _ in range(node_count + 1)]
for child_idx, parent_idx in enumerate(parent_list):
    child_sets[parent_idx].add(child_idx + 1)

level_nodes_list = [{0}]
while True:
    next_level_nodes = set()
    for parent_node in level_nodes_list[-1]:
        next_level_nodes.update(child_sets[parent_node])
    if not next_level_nodes:
        break
    level_nodes_list.append(next_level_nodes)
level_nodes_list.reverse()

level_widths = []
node_states = [None] * (node_count + 1)

for curr_level_idx, curr_level_nodes in enumerate(level_nodes_list):
    level_widths.append(len(curr_level_nodes))
    for curr_node in curr_level_nodes:
        node_child_set = child_sets[curr_node]
        if node_child_set:
            if len(node_child_set) == 1:
                only_child = node_child_set.pop()
                only_child_deque = node_states[only_child]
                only_child_deque.appendleft([1, 1, 0])
                node_states[curr_node] = only_child_deque
                continue
            child_deques = [node_states[child_node] for child_node in node_child_set]
            child_deques.sort(key=len)
            accumulated_deque = child_deques[0]
            for next_child_deque in child_deques[1:]:
                for (a0, a1, a2), b in zip(accumulated_deque, next_child_deque):
                    b[2] = ((a1 + a2) * b[1] + a2 * b[0]) % MODULO_VAL
                    b[1] = (a0 * b[1] + a1 * b[0]) % MODULO_VAL
                    b[0] = b[0] * a0 % MODULO_VAL
                accumulated_deque = next_child_deque
            for group in accumulated_deque:
                group[0] = (group[0] + group[2]) % MODULO_VAL
                group[2] = 0
            accumulated_deque.appendleft([1, 1, 0])
            node_states[curr_node] = accumulated_deque
        else:
            node_states[curr_node] = deque([[1, 1, 0]])

level_widths.reverse()

power_of_2 = power_cache_func_factory()
result_sum = sum(node_group[1] * power_of_2(node_count - level_idx + 1) % MODULO_VAL for level_idx, node_group in zip(level_widths, node_states[0])) % MODULO_VAL
print(result_sum)