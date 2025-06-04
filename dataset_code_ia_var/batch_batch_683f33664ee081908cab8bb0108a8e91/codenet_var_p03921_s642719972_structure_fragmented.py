def read_n_m():
    return map(int, input().split())

def create_parents_array(n):
    return [-1] * n

def uf_init_parents(self, n):
    self.n = n
    self.parents = create_parents_array(n)

def uf_find_rec(parents, x):
    if parents[x] < 0:
        return x
    parents[x] = uf_find_rec(parents, parents[x])
    return parents[x]

def uf_find(self, x):
    return uf_find_rec(self.parents, x)

def uf_union_find(self, x):
    return uf_find(self, x)

def uf_union(self, x, y):
    x = uf_union_find(self, x)
    y = uf_union_find(self, y)
    uf_union_core(self, x, y)

def uf_union_core(self, x, y):
    if x == y:
        return
    if self.parents[x] > self.parents[y]:
        x, y = y, x
    uf_merge(self, x, y)

def uf_merge(self, x, y):
    self.parents[x] += self.parents[y]
    self.parents[y] = x

def uf_size(self, x):
    return -self.parents[uf_find(self, x)]

def uf_same(self, x, y):
    return uf_find(self, x) == uf_find(self, y)

def uf_members(self, x):
    root = uf_find(self, x)
    return uf_member_list(self, root)

def uf_member_list(self, root):
    return [i for i in range(self.n) if uf_find(self, i) == root]

def uf_roots(self):
    return [i for i, x in enumerate(self.parents) if x < 0]

def uf_group_count(self):
    return len(uf_roots(self))

def uf_all_group_members(self):
    return {r: uf_members(self, r) for r in uf_roots(self)}

def uf_str(self):
    lines = []
    for r in uf_roots(self):
        lines.append('{}: {}'.format(r, uf_members(self, r)))
    return '\n'.join(lines)

class UnionFind():
    def __init__(self, n):
        uf_init_parents(self, n)
    def find(self, x):
        return uf_find(self, x)
    def union(self, x, y):
        uf_union(self, x, y)
    def size(self, x):
        return uf_size(self, x)
    def same(self, x, y):
        return uf_same(self, x, y)
    def members(self, x):
        return uf_members(self, x)
    def roots(self):
        return uf_roots(self)
    def group_count(self):
        return uf_group_count(self)
    def all_group_members(self):
        return uf_all_group_members(self)
    def __str__(self):
        return uf_str(self)

def read_people_lists(n):
    return [read_person_connections() for _ in range(n)]

def read_person_connections():
    a = list(map(int, input().split()))
    return a

def create_people_array(m):
    return [[] for _ in range(m)]

def process_connections(n, people, uf):
    for i in range(n):
        a = get_person_input()
        update_people(a, people, i, uf)

def get_person_input():
    a = list(map(int, input().split()))
    return a

def update_people(a, people, i, uf):
    n1 = a[0]
    a_rest = a[1:]
    for j in range(n1):
        updt_people_loop(a_rest, people, j, i, uf)

def updt_people_loop(a, people, j, i, uf):
    idx = a[j] - 1
    if len(people[idx]) == 0:
        people[idx].append(i)
    else:
        uf.union(people[idx][0], i)

def is_connected(uf):
    return uf.group_count() == 1

def main():
    n, m = read_n_m()
    uf = UnionFind(n)
    people = create_people_array(m)
    process_connections(n, people, uf)
    output_result(uf)

def output_result(uf):
    if is_connected(uf):
        print("YES")
    else:
        print("NO")

main()