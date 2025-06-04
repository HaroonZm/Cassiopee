node_count, set_count, operation_count = map(int, input().split())
*disjoint_parent_list, = range(node_count + set_count)

def find_root(node_index):
    if node_index == disjoint_parent_list[node_index]:
        return node_index
    disjoint_parent_list[node_index] = find_root(disjoint_parent_list[node_index])
    return disjoint_parent_list[node_index]

def union_sets(index_a, index_b):
    root_a = find_root(index_a)
    root_b = find_root(index_b)
    if root_a < root_b:
        disjoint_parent_list[root_b] = root_a
    else:
        disjoint_parent_list[root_a] = root_b

for operation_index in range(operation_count):
    operation_type, element_left, element_right = map(int, input().split())
    element_left -= 1
    element_right -= 1
    if operation_type == 1:
        set_left = find_root(set_count + element_left)
        set_right = find_root(set_count + element_right)
        if set_left < set_count and set_right < set_count and set_left != set_right:
            print(operation_index + 1)
            break
        union_sets(set_left, set_right)
    else:
        set_left = find_root(set_count + element_left)
        if set_left < set_count and set_left != element_right:
            print(operation_index + 1)
            break
        union_sets(element_right, set_left)
else:
    print(0)