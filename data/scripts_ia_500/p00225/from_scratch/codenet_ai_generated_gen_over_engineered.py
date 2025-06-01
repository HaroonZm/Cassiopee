class WordGraph:
    def __init__(self, words):
        self.words = words
        self.graph = {}
        self.in_degree = {}
        self.out_degree = {}
        self.nodes = set()
        self._build_graph()

    def _build_graph(self):
        for word in self.words:
            start = word[0]
            end = word[-1]
            self.nodes.add(start)
            self.nodes.add(end)
            self.graph.setdefault(start, []).append(end)
            self.out_degree[start] = self.out_degree.get(start, 0) + 1
            self.in_degree[end] = self.in_degree.get(end, 0) + 1

        # Ensure all nodes have in/out degree keys
        for node in self.nodes:
            self.in_degree.setdefault(node, 0)
            self.out_degree.setdefault(node, 0)

    def _is_strongly_connected(self):
        # Build adjacency and reverse adjacency with nodes having edges only
        adj = {node: [] for node in self.nodes}
        radj = {node: [] for node in self.nodes}
        for start in self.graph:
            for end in self.graph[start]:
                adj[start].append(end)
                radj[end].append(start)

        def dfs(graph, start, visited):
            stack = [start]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    stack.extend(graph[node])

        # Find a node with non-zero degree for start
        start_node = None
        for node in self.nodes:
            if self.out_degree[node] > 0:
                start_node = node
                break
        if start_node is None:
            return True   # No edges means trivially strongly connected

        visited = set()
        dfs(adj, start_node, visited)
        if any(self.out_degree[node] > 0 and node not in visited for node in self.nodes):
            return False

        visited.clear()
        dfs(radj, start_node, visited)
        if any(self.out_degree[node] > 0 and node not in visited for node in self.nodes):
            return False

        return True

    def _check_eulerian_circuit_conditions(self):
        # For Eulerian circuit in directed graph:
        # 1) Graph strongly connected (except isolated nodes)
        # 2) in_degree[node] == out_degree[node] for all nodes
        for node in self.nodes:
            if self.in_degree[node] != self.out_degree[node]:
                return False
        if not self._is_strongly_connected():
            return False
        return True


class ShiritoriSolver:
    def __init__(self, words):
        self.graph = WordGraph(words)

    def can_form_shiritori(self):
        return self.graph._check_eulerian_circuit_conditions()


class InputParser:
    def __init__(self):
        self.datasets = []

    def parse(self):
        import sys
        lines = sys.stdin.read().strip().split('\n')
        idx = 0
        while idx < len(lines):
            if lines[idx] == '0':
                break
            n = int(lines[idx])
            idx += 1
            words = []
            for _ in range(n):
                words.append(lines[idx])
                idx += 1
            self.datasets.append(words)


class ShiritoriController:
    def __init__(self):
        self.parser = InputParser()

    def run(self):
        self.parser.parse()
        for dataset in self.parser.datasets:
            solver = ShiritoriSolver(dataset)
            if solver.can_form_shiritori():
                print("OK")
            else:
                print("NG")


if __name__ == "__main__":
    controller = ShiritoriController()
    controller.run()