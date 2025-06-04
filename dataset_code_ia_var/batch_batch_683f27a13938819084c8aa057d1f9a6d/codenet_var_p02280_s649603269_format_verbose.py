MAX_NUMBER_OF_NODES = 10000
NO_PARENT_OR_CHILD = -1

class BinaryTreeNode:
    def __init__(self):
        self.parent_index = NO_PARENT_OR_CHILD
        self.left_child_index = 0
        self.right_child_index = 0

# Liste des profondeurs des nœuds (par index)
node_depths = [None for index in range(MAX_NUMBER_OF_NODES)]

# Liste des hauteurs des nœuds (par index)
node_heights = [None for index in range(MAX_NUMBER_OF_NODES)]

def assign_depth_recursively(node_index, current_depth):
    if node_index == NO_PARENT_OR_CHILD:
        return
    node_depths[node_index] = current_depth
    assign_depth_recursively(tree_nodes[node_index].left_child_index, current_depth + 1)
    assign_depth_recursively(tree_nodes[node_index].right_child_index, current_depth + 1)

def assign_height_recursively(node_index):
    left_height = 0
    right_height = 0

    if tree_nodes[node_index].left_child_index != NO_PARENT_OR_CHILD:
        left_height = assign_height_recursively(tree_nodes[node_index].left_child_index) + 1
    if tree_nodes[node_index].right_child_index != NO_PARENT_OR_CHILD:
        right_height = assign_height_recursively(tree_nodes[node_index].right_child_index) + 1

    node_heights[node_index] = max(left_height, right_height)
    return node_heights[node_index]

def find_sibling_index(node_index):
    parent_index = tree_nodes[node_index].parent_index
    if parent_index == NO_PARENT_OR_CHILD:
        return NO_PARENT_OR_CHILD

    parent_node = tree_nodes[parent_index]

    if parent_node.left_child_index != node_index and parent_node.left_child_index != NO_PARENT_OR_CHILD:
        return parent_node.left_child_index
    if parent_node.right_child_index != node_index and parent_node.right_child_index != NO_PARENT_OR_CHILD:
        return parent_node.right_child_index

    return NO_PARENT_OR_CHILD

number_of_nodes = int(input())

tree_nodes = []

for i in range(number_of_nodes):
    node = BinaryTreeNode()
    tree_nodes.append(node)

def display_node_details(node_index):
    degree = 0
    if tree_nodes[node_index].left_child_index != NO_PARENT_OR_CHILD:
        degree += 1
    if tree_nodes[node_index].right_child_index != NO_PARENT_OR_CHILD:
        degree += 1

    print(
        "node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, ".format(
            node_index,
            tree_nodes[node_index].parent_index,
            find_sibling_index(node_index),
            degree,
            node_depths[node_index],
            node_heights[node_index]
        ),
        end=""
    )

    is_root = tree_nodes[node_index].parent_index == NO_PARENT_OR_CHILD
    is_leaf = (
        tree_nodes[node_index].left_child_index == NO_PARENT_OR_CHILD and
        tree_nodes[node_index].right_child_index == NO_PARENT_OR_CHILD
    )

    if is_root:
        print("root")
    elif is_leaf:
        print("leaf")
    else:
        print("internal node")

for i in range(number_of_nodes):
    current_node_index, left_child_index, right_child_index = map(int, input().split())
    tree_nodes[current_node_index].left_child_index = left_child_index
    tree_nodes[current_node_index].right_child_index = right_child_index

    if left_child_index != NO_PARENT_OR_CHILD:
        tree_nodes[left_child_index].parent_index = current_node_index
    if right_child_index != NO_PARENT_OR_CHILD:
        tree_nodes[right_child_index].parent_index = current_node_index

for i in range(number_of_nodes):
    if tree_nodes[i].parent_index == NO_PARENT_OR_CHILD:
        root_index = i
        assign_depth_recursively(root_index, 0)
        assign_height_recursively(root_index)

for i in range(number_of_nodes):
    display_node_details(i)