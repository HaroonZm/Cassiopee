class Entity:
    def __init__(self, id_):
        self.id = id_

class Student(Entity):
    def __init__(self, id_):
        super().__init__(id_)

class Club(Entity):
    def __init__(self, id_):
        super().__init__(id_)

class MembershipManager:
    def __init__(self, num_students, num_clubs):
        self.num_students = num_students
        self.num_clubs = num_clubs
        # We create a union-find structure with 2*N elements:
        # For each student s in [1..N], s represents "student s",
        # and s+N represents "club of student s".
        # We use this encoding to relate students and their clubs consistently.
        self.uf = UnionFind(num_students * 2 + 1)

    def _student_id(self, s_id):
        return s_id

    def _club_id(self, s_id):
        return s_id + self.num_students

    def union_students_same_club(self, a, b):
        # a and b are students, they must belong to the same club
        ua1 = self.uf.find(self._student_id(a))
        ua2 = self.uf.find(self._club_id(a))
        ub1 = self.uf.find(self._student_id(b))
        ub2 = self.uf.find(self._club_id(b))
        # To be consistent, either both a,b have the same club root, or both have their 'club' nodes connected
        # We union student nodes with their respective club nodes.
        # Check if a is clubed with b conflicted:
        # If student a's student node is connected to student b's club node means conflict
        if self.uf.same(ua1, ub2) or self.uf.same(ua2, ub1):
            return False
        # Union their student IDs
        self.uf.union(ua1, ub1)
        # Union their club IDs so that clubs match
        self.uf.union(ua2, ub2)
        return True

    def union_student_with_club(self, c, x):
        # student c belongs to club x
        # We'll interpret club x as entity (num_students + N + x),
        # but input clubs go from 1..M, so we offset clubs by (2*N)
        club_offset = 2 * self.num_students
        club_x_id = club_offset + x
        # Ensure union-find has enough capacity:
        if club_x_id >= self.uf.size:
            self.uf.extend(club_x_id)

        sc = self._student_id(c)
        cc = club_x_id
        # Check if c is already connected to a conflicting club:
        # If c's club node is connected to another club, conflict if not same
        # Check if student node and this club node conflict with existing connections:
        # If student node connected to other club nodes different than this one, conflict.
        # We'll check by disallowing union if this new club conflicts with previous ones
        if self.uf.same(sc, cc + self.num_students) or self.uf.same(sc + self.num_students, cc):
            return False
        # We union student's club node with club_x_id node.
        # Also, link student's student node with its club node.
        self.uf.union(sc + self.num_students, cc)
        self.uf.union(sc, sc)
        return True

class UnionFind:
    def __init__(self, n):
        self.size = n
        self.parent = list(range(n))
        self.rank = [0] * n

    def extend(self, new_size):
        if new_size < self.size:
            return
        extension = new_size + 1 - self.size
        self.parent.extend(range(self.size, new_size + 1))
        self.rank.extend([0] * extension)
        self.size = new_size + 1

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        else:
            self.parent[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

class RecordProcessor:
    def __init__(self, n_students, m_clubs, k_records):
        self.n = n_students
        self.m = m_clubs
        self.k = k_records
        self.mem_manager = MembershipManager(n_students, m_clubs)
        self.conflict_line = 0

    def process_records(self, records):
        # Club ids are needed for union-find indexing large enough to hold
        # We'll interpret clubs with an offset from 2N + 1 upwards
        # For union-find, we prepare that capacity upfront to avoid complexities
        # We'll implement a more consistent approach:
        # For each student s:
        # - node s : student node
        # - node s+N: club node belonging to student s
        # For each club x:
        # - node 2N + x : club node
        # union student s's club node with club x to enforce membership
        offset_clubs = 2 * self.n
        max_club_node = offset_clubs + self.m + 1
        # Extend union-find accordingly
        self.mem_manager.uf.extend(max_club_node)

        for i, line in enumerate(records, 1):
            parts = line.split()
            t = int(parts[0])
            if t == 1:
                a = int(parts[1])
                b = int(parts[2])
                if not self._process_type1(a, b):
                    self.conflict_line = i
                    break
            else:
                c = int(parts[1])
                x = int(parts[2])
                if not self._process_type2(c, x):
                    self.conflict_line = i
                    break

    def _process_type1(self, a, b):
        # a,b same club
        uf = self.mem_manager.uf
        n = self.n
        # Find root of a student and b student
        sa = uf.find(a)
        sca = uf.find(a + n)
        sb = uf.find(b)
        scb = uf.find(b + n)
        # Conflict if a is in club of b but also in different:
        # If student's student node connected to other's club node conflict
        # Equivalent to if sa connected to scb or sb connected to sca
        if uf.same(sa, scb) or uf.same(sb, sca):
            return False
        # Union the student nodes
        uf.union(sa, sb)
        # Union their club nodes
        uf.union(sca, scb)
        return True

    def _process_type2(self, c, x):
        uf = self.mem_manager.uf
        n = self.n
        offset_club = 2 * n
        sc = c
        scc = c + n
        club_id = offset_club + x
        # Check conflict:
        # If student's student node connected with club node of some other club,
        # that means conflict if that club node is not club_id
        # to check conflict:
        # If student's club node connected to a different club node than club_id
        # we detect conflict:
        # So if student's club node is connected to club nodes other than club_id => conflict
        # But union-find merges all club nodes connected, so just check if student's club node
        # has a root different than club_id.
        if uf.same(sc, club_id):
            # already belongs to this club, no conflict
            return True
        # If student's club node belongs to other club node != club_id, conflict
        for c_id in range(offset_club + 1, offset_club + self.m + 1):
            if c_id != club_id and uf.same(scc, c_id):
                return False
        # Now union student's club node with club_id node
        uf.union(scc, club_id)
        # Also union student's student node with its club node to fix links
        uf.union(sc, sc)
        return True

def main():
    import sys
    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    records = [input().strip() for _ in range(k)]
    processor = RecordProcessor(n, m, k)
    processor.process_records(records)
    print(processor.conflict_line)

if __name__ == "__main__":
    main()