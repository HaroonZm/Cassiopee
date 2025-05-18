#!/usr/bin/env python3

import array

class UnionFind(object):

    def __init__(self, number_of_nodes, typecode="L"):
        self.typecode = typecode
        self.par = array.array(typecode, range(number_of_nodes))
        self.rank = array.array(typecode, (0 for i in range(number_of_nodes)))

    def root(self, node):
        if self.par[node] == node:
            return node
        else:
            r = self.root(self.par[node])
            self.par[node] = r
            return r

    def in_the_same_set(self, node1, node2):
        return self.root(node1) == self.root(node2)

    def unite(self, node1, node2):
        x = self.root(node1)
        y = self.root(node2)
        if x == y:
            pass
        elif self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

def main():
    n, m = map(int, input().split())
    uf = UnionFind(n, "I")
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        uf.unite(a, b)
    city_representatives = set()
    num_cities_and_villages = 0
    for i in range(n):
        rep = uf.root(i)
        if i == rep:
            num_cities_and_villages += 1
        else:
            city_representatives.add(rep)
    num_cities = len(city_representatives)
    answer = abs(num_cities_and_villages - 2 * num_cities)
    print(answer)

if __name__ == '__main__':
    main()