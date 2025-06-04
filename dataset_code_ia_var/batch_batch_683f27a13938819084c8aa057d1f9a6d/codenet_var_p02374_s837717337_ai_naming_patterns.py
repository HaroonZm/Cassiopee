NODE_CAPACITY = 10 ** 5
parent_node = [0] * (NODE_CAPACITY + 1)
left_child = [-1] + [0] * NODE_CAPACITY
right_child = [-1] + [0] * NODE_CAPACITY
subtree_size = [0] + [1] * NODE_CAPACITY
node_key = [0] * (NODE_CAPACITY + 1)
subtree_value = [0] * (NODE_CAPACITY + 1)
reverse_flag = [0] * (NODE_CAPACITY + 1)

def node_update(node_idx, left_idx, right_idx):
    subtree_size[node_idx] = 1 + subtree_size[left_idx] + subtree_size[right_idx]
    subtree_value[node_idx] = node_key[node_idx] + subtree_value[left_idx] + subtree_value[right_idx]

def node_swap(node_idx):
    if node_idx:
        left_child[node_idx], right_child[node_idx] = right_child[node_idx], left_child[node_idx]
        reverse_flag[node_idx] ^= 1

def node_propagate(node_idx):
    node_swap(left_child[node_idx])
    node_swap(right_child[node_idx])
    reverse_flag[node_idx] = 0
    return 1

def node_splay(node_idx):
    curr_parent = parent_node[node_idx]
    if reverse_flag[node_idx]:
        node_propagate(node_idx)

    left_idx = left_child[node_idx]
    right_idx = right_child[node_idx]
    while curr_parent and not left_child[curr_parent] != node_idx != right_child[curr_parent]:
        grandparent = parent_node[curr_parent]
        if not grandparent or left_child[grandparent] != curr_parent != right_child[grandparent]:
            if reverse_flag[curr_parent] and node_propagate(curr_parent):
                left_idx, right_idx = right_idx, left_idx
                node_swap(left_idx)
                node_swap(right_idx)

            if left_child[curr_parent] == node_idx:
                left_child[curr_parent] = right_idx
                parent_node[right_idx] = curr_parent
                node_update(curr_parent, right_idx, right_child[curr_parent])
                right_idx = curr_parent
            else:
                right_child[curr_parent] = left_idx
                parent_node[left_idx] = curr_parent
                node_update(curr_parent, left_child[curr_parent], left_idx)
                left_idx = curr_parent
            curr_parent = grandparent
            break

        if reverse_flag[grandparent]:
            node_propagate(grandparent)
        if reverse_flag[curr_parent]:
            node_propagate(curr_parent)
            left_idx, right_idx = right_idx, left_idx
            node_swap(left_idx)
            node_swap(right_idx)

        ancestor = parent_node[grandparent]
        if left_child[grandparent] == curr_parent:
            if left_child[curr_parent] == node_idx:
                temp = left_child[grandparent] = right_child[curr_parent]
                parent_node[temp] = grandparent
                node_update(grandparent, temp, right_child[grandparent])

                left_child[curr_parent] = right_idx
                right_child[curr_parent] = grandparent
                parent_node[right_idx] = curr_parent
                node_update(curr_parent, right_idx, grandparent)

                parent_node[grandparent] = right_idx = curr_parent
            else:
                left_child[grandparent] = right_idx
                parent_node[right_idx] = grandparent
                node_update(grandparent, right_idx, right_child[grandparent])

                right_child[curr_parent] = left_idx
                parent_node[left_idx] = curr_parent
                node_update(curr_parent, left_child[curr_parent], left_idx)

                left_idx = curr_parent
                right_idx = grandparent
        else:
            if right_child[curr_parent] == node_idx:
                temp = right_child[grandparent] = left_child[curr_parent]
                parent_node[temp] = grandparent
                node_update(grandparent, left_child[grandparent], temp)

                left_child[curr_parent] = grandparent
                right_child[curr_parent] = left_idx
                parent_node[left_idx] = curr_parent
                node_update(curr_parent, grandparent, left_idx)

                parent_node[grandparent] = left_idx = curr_parent
            else:
                right_child[grandparent] = left_idx
                parent_node[left_idx] = grandparent
                node_update(grandparent, left_child[grandparent], left_idx)

                left_child[curr_parent] = right_idx
                parent_node[right_idx] = curr_parent
                node_update(curr_parent, right_idx, right_child[curr_parent])

                left_idx = grandparent
                right_idx = curr_parent

        curr_parent = ancestor
        if left_child[ancestor] == grandparent:
            left_child[ancestor] = node_idx
            node_update(ancestor, node_idx, right_child[ancestor])
        elif right_child[ancestor] == grandparent:
            right_child[ancestor] = node_idx
            node_update(ancestor, left_child[ancestor], node_idx)
        else:
            break

    node_update(node_idx, left_idx, right_idx)
    left_child[node_idx] = left_idx
    right_child[node_idx] = right_idx
    parent_node[left_idx] = parent_node[right_idx] = node_idx
    parent_node[node_idx] = curr_parent

    reverse_flag[node_idx] = parent_node[0] = 0

def node_expose(node_idx):
    prev_idx = 0
    curr_idx = node_idx
    while curr_idx:
        node_splay(curr_idx)
        right_child[curr_idx] = prev_idx
        node_update(curr_idx, left_child[curr_idx], prev_idx)
        prev_idx = curr_idx
        curr_idx = parent_node[curr_idx]
    node_splay(node_idx)
    return node_idx

def node_cut(node_idx):
    node_expose(node_idx)
    parent_idx = left_child[node_idx]
    left_child[node_idx] = parent_node[parent_idx] = 0
    return parent_idx

def node_link(child_idx, parent_idx):
    node_expose(child_idx)
    node_expose(parent_idx)
    parent_node[child_idx] = parent_idx
    right_child[parent_idx] = child_idx

def node_evert(node_idx):
    node_expose(node_idx)
    node_swap(node_idx)
    if reverse_flag[node_idx]:
        node_propagate(node_idx)

def node_query(query_idx):
    result_node = node_expose(query_idx + 1)
    return subtree_value[result_node]

def node_key_add(query_idx, add_value):
    node_key[query_idx + 1] += add_value
    node_expose(query_idx + 1)

input_read = open(0).readline
output_write = open(1, 'w').writelines

node_count = int(input_read())
for idx in range(node_count):
    input_data = list(map(int, input_read().split()))
    child_count = input_data[0]
    child_list = input_data[1:]
    if child_count:
        node_expose(idx + 1)
        for child in child_list:
            node_expose(child + 1)
            parent_node[child + 1] = idx + 1
        right_child[idx + 1] = child_list[0] + 1

query_count = int(input_read())
result_buffer = []
for _ in range(query_count):
    query_data = list(map(int, input_read().split()))
    query_type = query_data[0]
    query_args = query_data[1:]
    if query_type:
        result_buffer.append("%d\n" % node_query(query_args[0]))
    else:
        node_key_add(*query_args)
output_write(result_buffer)