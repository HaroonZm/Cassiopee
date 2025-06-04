MOD_CONST = 1000000007

class TreeNode:
    def __init__(self, node_type, child_nodes=None, cached_value=None, child_indices=None):
        self.node_type = node_type
        self.child_nodes = [] if child_nodes is None else child_nodes
        self.child_indices = [] if child_indices is None else child_indices
        self.cached_value = cached_value

    def compute_case_count(self):
        if self.cached_value is not None:
            return self.cached_value

        case_values = self._yield_child_case_counts()
        if "E" in self.node_type:
            total = compute_modular_product(case_values)
            if "?" in self.node_type:
                total += 1
            return total % MOD_CONST

        elif "A" in self.node_type:
            total = sum(case_values)
            if "?" in self.node_type:
                total += 1
            return total % MOD_CONST

        elif "R" in self.node_type:
            total = compute_modular_product((count+1 for count in case_values))
            if "?" not in self.node_type:
                total -= 1
            return total % MOD_CONST

        else:
            raise ValueError("Invalid node_type.")

    def _yield_child_case_counts(self):
        for child_node in self.child_nodes:
            yield child_node.compute_case_count()

    def is_terminal_parent(self):
        return self.child_nodes and all(not child.child_nodes for child in self.child_nodes)

def compute_modular_product(values_iterable):
    result = 1
    for value in values_iterable:
        result = (result * (value % MOD_CONST)) % MOD_CONST
    return result

def perform_single_reduction_step(tree_nodes):
    terminal_parent_nodes = [node for node in tree_nodes if node is not None and node.is_terminal_parent()]
    for parent_node in terminal_parent_nodes:
        parent_node.cached_value = parent_node.compute_case_count()
        parent_node.child_nodes.clear()
        for idx in parent_node.child_indices:
            tree_nodes[idx] = None
    return tree_nodes

def reduce_tree_to_root(tree_nodes):
    while tree_nodes[1:] != [None] * (len(tree_nodes) - 1):
        tree_nodes = perform_single_reduction_step(tree_nodes)
    return tree_nodes[0]

def main_routine():
    total_nodes = int(input())
    tree_nodes = []
    for _ in range(total_nodes):
        node_type_input = input()
        tree_nodes.append(TreeNode(node_type_input))
    for _ in range(total_nodes - 1):
        parent_idx, child_idx = (int(x) for x in input().split())
        tree_nodes[parent_idx - 1].child_nodes.append(tree_nodes[child_idx - 1])
        tree_nodes[parent_idx - 1].child_indices.append(child_idx - 1)

    root_node = reduce_tree_to_root(tree_nodes)
    print(root_node.cached_value % MOD_CONST)

if __name__ == '__main__':
    main_routine()