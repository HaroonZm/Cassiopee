class DisjointSetUnion:
    def __init__(self, node_count):
        self.parent_or_size = [-1] * node_count

    def root(self, node):
        while self.parent_or_size[node] >= 0:
            node = self.parent_or_size[node]
        return node

    def unite(self, node_a, node_b):
        root_a = self.root(node_a)
        root_b = self.root(node_b)
        if root_a != root_b:
            if self.parent_or_size[root_a] < self.parent_or_size[root_b]:
                self.parent_or_size[root_a] += self.parent_or_size[root_b]
                self.parent_or_size[root_b] = root_a
            else:
                self.parent_or_size[root_b] += self.parent_or_size[root_a]
                self.parent_or_size[root_a] = root_b

    def are_disjoint(self, node_a, node_b):
        return self.root(node_a) != self.root(node_b)

def process_island_problem():
    import sys
    input_lines = sys.stdin.readlines()
    from bisect import bisect_left
    from itertools import filterfalse

    while True:
        island_count, bridge_count = map(int, input_lines[0].split())
        if island_count == 0 and bridge_count == 0:
            break

        removal_order = list(map(int, input_lines[1:1+island_count]))
        island_info = list(zip(removal_order, range(1, island_count + 1)))
        island_info.sort()
        flood_days, island_ids = zip(*island_info)

        bridge_records = [tuple(map(int, line.split())) for line in input_lines[1+island_count:1+island_count+bridge_count]]
        bridge_records.sort(key=lambda bridge_triplet: bridge_triplet[2])

        dsu = DisjointSetUnion(island_count + 1)
        total_cost = 0
        current_island_idx = island_count
        is_mst_ongoing = True
        available_bridges = bridge_records.copy()

        while current_island_idx > 0:
            if is_mst_ongoing:
                current_island_idx -= 1
                current_island_idx = bisect_left(flood_days, flood_days[current_island_idx])
                active_islands = island_ids[current_island_idx:]

                def valid_bridge_for_active(bridge):
                    return bridge[0] in active_islands and bridge[1] in active_islands

                active_bridges = filter(valid_bridge_for_active, bridge_records)
                required_bridges = len(active_islands) - 1
                connected_bridges = 0

                for bridge in active_bridges:
                    node1, node2, bridge_cost = bridge
                    if dsu.are_disjoint(node1, node2):
                        dsu.unite(node1, node2)
                        total_cost += bridge_cost
                        connected_bridges += 1
                        if connected_bridges == required_bridges:
                            is_mst_ongoing = False
                            break
                else:
                    is_mst_ongoing = True
                    dsu = DisjointSetUnion(island_count + 1)
                    total_cost = 0
            else:
                upper_idx = current_island_idx
                current_island_idx -= 1
                current_island_idx = bisect_left(flood_days, flood_days[current_island_idx])
                existing_islands = island_ids[current_island_idx:]
                flooded_islands = island_ids[upper_idx:]

                def active_bridge_for_existing(bridge):
                    return bridge[0] in existing_islands and bridge[1] in existing_islands

                filtered_bridges = filter(active_bridge_for_existing, bridge_records)

                def not_bridge_for_flooded(bridge):
                    return bridge[0] in flooded_islands and bridge[1] in flooded_islands

                filtered_bridges = filterfalse(not_bridge_for_flooded, filtered_bridges)
                new_required_bridges = upper_idx - current_island_idx
                new_connected_bridges = 0

                for bridge in filtered_bridges:
                    node1, node2, bridge_cost = bridge
                    if dsu.are_disjoint(node1, node2):
                        dsu.unite(node1, node2)
                        total_cost += bridge_cost
                        new_connected_bridges += 1
                        if new_connected_bridges == new_required_bridges:
                            break
                else:
                    is_mst_ongoing = True
                    dsu = DisjointSetUnion(island_count + 1)
                    total_cost = 0

        if -island_count in dsu.parent_or_size:
            print(total_cost)
        else:
            print(0)

        del input_lines[:island_count + 1 + bridge_count]

process_island_problem()