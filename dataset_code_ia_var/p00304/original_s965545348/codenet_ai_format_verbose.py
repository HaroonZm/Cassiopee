# encoding: 'utf-8'

MODULO_FOR_RESULT = 1000000007

class TreeNode:
    """Class representing a node in the tree with its associated attributes and logic."""

    def __init__(self, node_type, child_nodes=None, computed_cases=None, indices_of_children=None):
        self.node_type = node_type
        if child_nodes is None:
            child_nodes = []
        if indices_of_children is None:
            indices_of_children = []
        self.child_nodes = child_nodes
        self.indices_of_children = indices_of_children
        self.computed_cases = None

    def compute_number_of_cases(self):
        """Calculate the number of cases recursively for this node."""
        if self.computed_cases is not None:
            return self.computed_cases

        cases_for_children = list(self.generate_cases_for_children())

        if "E" in self.node_type:
            total_cases = compute_product_modulo(cases_for_children)
            if "?" in self.node_type:
                total_cases += 1
            return total_cases % MODULO_FOR_RESULT

        elif "A" in self.node_type:
            total_cases = sum(cases_for_children)
            if "?" in self.node_type:
                total_cases += 1
            return total_cases % MODULO_FOR_RESULT

        elif "R" in self.node_type:
            total_cases = compute_product_modulo((child_case + 1 for child_case in cases_for_children))
            if "?" not in self.node_type:
                total_cases -= 1
            return total_cases % MODULO_FOR_RESULT

        else:
            raise Exception("Encountered invalid node type.")

    def generate_cases_for_children(self):
        """Yield the computed number of cases for each child node."""
        for child_node in self.child_nodes:
            yield child_node.compute_number_of_cases()

    def is_parent_of_leaves(self):
        """Return True if all direct children are leaf nodes (i.e., have no children of their own)."""
        has_children = bool(self.child_nodes)
        all_children_are_leaves = all(child.child_nodes == [] for child in self.child_nodes)
        return has_children and all_children_are_leaves

def compute_product_modulo(sequence):
    """Compute the product of all elements in a sequence, modulo MODULO_FOR_RESULT."""
    result_product = 1
    for value in sequence:
        result_product = (result_product * (value % MODULO_FOR_RESULT)) % MODULO_FOR_RESULT
    return result_product

def collapse_last_parents_in_tree(list_of_nodes):
    """Collapse all parents whose children are leaves, updating their case count and removing their children."""
    last_parents = [
        node for node in list_of_nodes
        if node is not None and node.is_parent_of_leaves()
    ]

    for parent_node in last_parents:
        parent_node.computed_cases = parent_node.compute_number_of_cases()
        parent_node.child_nodes = []
        for child_index in parent_node.indices_of_children:
            list_of_nodes[child_index] = None

    return list_of_nodes

def collapse_tree_to_root(list_of_nodes):
    """Repeatedly collapse the tree by merging last parents until only the root remains."""
    while list_of_nodes[1:] != [None] * (len(list_of_nodes) - 1):
        list_of_nodes = collapse_last_parents_in_tree(list_of_nodes)
    return list_of_nodes[0]

def main():
    """Main function to read input, build tree, and output the result."""
    number_of_nodes = int(input())
    all_nodes_in_tree = []

    for _ in range(number_of_nodes):
        node_type_str = input()
        all_nodes_in_tree.append(TreeNode(node_type_str))

    for _ in range(number_of_nodes - 1):
        parent_index, child_index = (int(x) for x in input().split())
        all_nodes_in_tree[parent_index - 1].child_nodes.append(all_nodes_in_tree[child_index - 1])
        all_nodes_in_tree[parent_index - 1].indices_of_children.append(child_index - 1)

    root_result_node = collapse_tree_to_root(all_nodes_in_tree)
    print(root_result_node.computed_cases % MODULO_FOR_RESULT)

if __name__ == '__main__':
    main()