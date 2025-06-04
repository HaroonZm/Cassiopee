def main():
    while True:

        input_line_tokens = raw_input().split()
        while input_line_tokens == []:
            input_line_tokens = raw_input().split()

        if input_line_tokens[0] == "0":
            break

        number_of_moves_in_first_sequence = int(input_line_tokens[0])
        moves_for_first_sequence = input_line_tokens[1:]

        while len(moves_for_first_sequence) < number_of_moves_in_first_sequence:
            moves_for_first_sequence += raw_input().split()

        original_key_graph_nodes = construct_key_graph(moves_for_first_sequence)

        input_line_tokens = raw_input().split()
        while input_line_tokens == []:
            input_line_tokens = raw_input().split()

        number_of_moves_in_second_sequence = int(input_line_tokens[0])
        moves_for_second_sequence = input_line_tokens[1:]

        while len(moves_for_second_sequence) < number_of_moves_in_second_sequence:
            moves_for_second_sequence += raw_input().split()

        transformed_key_graph_nodes = construct_key_graph(moves_for_second_sequence)

        for rotated_nodes in generate_all_possible_rotations(transformed_key_graph_nodes):
            if key_structures_are_equivalent(original_key_graph_nodes, rotated_nodes):
                print "SAME"
                break
        else:
            print "DIFFERENT"


def key_structures_are_equivalent(reference_key_nodes, other_key_nodes):
    def depth_first_verification(node_in_reference_key, node_in_other_key):
        already_visited_in_reference = node_in_reference_key in visited_reference_nodes
        already_visited_in_other = node_in_other_key in visited_other_nodes

        if already_visited_in_reference != already_visited_in_other:
            return False

        if already_visited_in_reference and already_visited_in_other:
            return True

        visited_reference_nodes[node_in_reference_key] = True
        visited_other_nodes[node_in_other_key] = True

        for edge_direction in node_in_reference_key.edges.keys():
            reference_edge_node = node_in_reference_key.edges[edge_direction]
            other_edge_node = node_in_other_key.edges[edge_direction]

            if reference_edge_node is None:
                if other_edge_node is not None:
                    return False
            elif other_edge_node is None:
                return False
            elif not depth_first_verification(reference_edge_node, other_edge_node):
                return False
        return True

    for candidate_start_node_in_other_key in other_key_nodes:
        visited_reference_nodes = {}
        visited_other_nodes = {}
        if depth_first_verification(reference_key_nodes[0], candidate_start_node_in_other_key):
            return True
    return False


def construct_key_graph(sequence_of_moves):
    axis_incremental_moves = {"+x": (1, 0, 0), "-x": (-1, 0, 0),
                              "+y": (0, 1, 0), "-y": (0, -1, 0),
                              "+z": (0, 0, 1), "-z": (0, 0, -1)}
    opposite_axises = {"+x": "-x", "-x": "+x",
                       "+y": "-y", "-y": "+y",
                       "+z": "-z", "-z": "+z"}
    label_to_node_mapping = {}
    previous_node = KeyNode([0, 0, 0])
    coordinate_to_node_mapping = {previous_node: previous_node}
    for move_token in sequence_of_moves:
        if move_token.isdigit():
            if move_token in label_to_node_mapping:
                previous_node = label_to_node_mapping[move_token]
            else:
                label_to_node_mapping[move_token] = previous_node
        else:
            next_node_coordinates = [previous_node[dimension_index] + axis_incremental_moves[move_token][dimension_index] for dimension_index in xrange(3)]
            next_node_candidate = KeyNode(next_node_coordinates)
            if next_node_candidate in coordinate_to_node_mapping:
                next_node_candidate = coordinate_to_node_mapping[next_node_candidate]
            else:
                coordinate_to_node_mapping[next_node_candidate] = next_node_candidate
            previous_node.add_edge(move_token, next_node_candidate)
            next_node_candidate.add_edge(opposite_axises[move_token], previous_node)
            previous_node = next_node_candidate
    return coordinate_to_node_mapping.values()


def generate_all_possible_rotations(list_of_key_nodes):
    rotation_schedule = (
        KeyNode.rotate_x, KeyNode.rotate_x, KeyNode.rotate_x, KeyNode.rotate_x, 
        KeyNode.rotate_y, KeyNode.rotate_z, KeyNode.rotate_z, KeyNode.rotate_z, KeyNode.rotate_z,
        KeyNode.rotate_y, KeyNode.rotate_x, KeyNode.rotate_x, KeyNode.rotate_x, KeyNode.rotate_x,
        KeyNode.rotate_y, KeyNode.rotate_z, KeyNode.rotate_z, KeyNode.rotate_z, KeyNode.rotate_z,
        KeyNode.rotate_x, KeyNode.rotate_y, KeyNode.rotate_y, KeyNode.rotate_y, KeyNode.rotate_y,
        KeyNode.rotate_x, KeyNode.rotate_z, KeyNode.rotate_z, KeyNode.rotate_z, KeyNode.rotate_z,
        KeyNode.rotate_x, KeyNode.rotate_y, KeyNode.rotate_y, KeyNode.rotate_y, KeyNode.rotate_y
    )
    for rotate_function in rotation_schedule:
        rotate_function(list_of_key_nodes[0], {})
        yield list_of_key_nodes


class KeyNode(tuple):

    def __init__(self, xyz_coordinates_list):
        if len(xyz_coordinates_list) != 3:
            raise ValueError("Each KeyNode must represent a 3D point.")
        tuple.__init__(self, xyz_coordinates_list)
        self.edges = dict((direction_label, None) for direction_label in ["+x", "-x", "+y", "-y", "+z", "-z"])

    def add_edge(self, edge_direction, neighbor_node):
        if edge_direction not in self.edges:
            raise ValueError("Invalid edge direction: " + edge_direction)
        self.edges[edge_direction] = neighbor_node

    @classmethod
    def rotate_x(cls, target_node, visited_nodes={}):
        if target_node in visited_nodes:
            return []
        visited_nodes[tuple(target_node)] = target_node
        target_node.edges["+y"], target_node.edges["+z"], target_node.edges["-y"], target_node.edges["-z"] = \
            target_node.edges["-z"], target_node.edges["+y"], target_node.edges["+z"], target_node.edges["-y"]
        for neighboring_node in target_node.edges.values():
            if neighboring_node is not None:
                cls.rotate_x(neighboring_node, visited_nodes)

    @classmethod
    def rotate_y(cls, target_node, visited_nodes={}):
        if target_node in visited_nodes:
            return []
        visited_nodes[tuple(target_node)] = target_node
        target_node.edges["+x"], target_node.edges["+z"], target_node.edges["-x"], target_node.edges["-z"] = \
            target_node.edges["-z"], target_node.edges["+x"], target_node.edges["+z"], target_node.edges["-x"]
        for neighboring_node in target_node.edges.values():
            if neighboring_node is not None:
                cls.rotate_y(neighboring_node, visited_nodes)

    @classmethod
    def rotate_z(cls, target_node, visited_nodes={}):
        if target_node in visited_nodes:
            return []
        visited_nodes[tuple(target_node)] = target_node
        target_node.edges["+x"], target_node.edges["+y"], target_node.edges["-x"], target_node.edges["-y"] = \
            target_node.edges["-y"], target_node.edges["+x"], target_node.edges["+y"], target_node.edges["-x"]
        for neighboring_node in target_node.edges.values():
            if neighboring_node is not None:
                cls.rotate_z(neighboring_node, visited_nodes)

    @classmethod
    def traverse_entire_graph(cls, start_node, visited_nodes={}):
        if start_node in visited_nodes:
            return []
        visited_nodes[tuple(start_node)] = start_node
        collected_nodes = [start_node]
        for neighbor in start_node.edges.values():
            if neighbor is not None:
                collected_nodes += cls.traverse_entire_graph(neighbor, visited_nodes + [start_node])
        return collected_nodes


if __name__ == "__main__":
    main()