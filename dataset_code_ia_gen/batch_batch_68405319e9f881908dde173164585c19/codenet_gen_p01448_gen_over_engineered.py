class RangeConstraint:
    def __init__(self, min_people: int, max_people: int):
        self.min_people = min_people
        self.max_people = max_people

    def is_satisfied(self, total_people: int) -> bool:
        return self.min_people <= total_people <= self.max_people


class Friend:
    def __init__(self, constraint: RangeConstraint):
        self.constraint = constraint

    def is_happy(self, total_people: int) -> bool:
        return self.constraint.is_satisfied(total_people)


class FriendGroup:
    def __init__(self):
        self.friends = []

    def add_friend(self, friend: Friend):
        self.friends.append(friend)

    def max_invite(self) -> int:
        # total_people = invited friends + 1 (myself)
        N = len(self.friends)
        
        # We want to select k friends s.t. for all selected i:
        # a_i <= k+1 <= b_i
        # == a_i <= k+1 and k+1 <= b_i
        # Because all selected friends must be happy,
        # k+1 must be at least max of a_i among chosen friends, and at most min of b_i among chosen friends.

        # Approach: since we want max k,
        # we test k from N down to 0, for each k check if there are at least k friends with a_i <= k+1 <= b_i.

        # To optimise:
        # For each friend, can they be happy with total = k+1?
        # So for each k, count friends with a_i <= k+1 <= b_i

        # Since N can be 1e5, naive O(N^2) would be too slow.

        # Optimization:
        # Let's sort friends by a_i ascending.

        # For each k from N down to 0:
        # We fix total = k+1
        # count how many friends satisfy a_i <= total <= b_i

        # To speed up, we can:
        # 1) For each friend, record (a_i, b_i)
        # 2) We want to quickly find counts of friends with a_i <= total and b_i >= total.

        # We can preprocess:
        # - Sort friends by a_i ascending
        # - Prepare a binary indexed tree or segment tree on b_i to count how many friends with b_i >= total among those with a_i <= total
        # But b_i max is up to 100001, we can manage that.

        # Alternative simplification:
        # Because a_i <= b_i
        # For each total = k+1, we want to know how many friends satisfy a_i <= total <= b_i.

        # So, both conditions must hold.

        # Since we check multiple totals from large to small, we can build index for a_i and b_i.

        # Another approach: For all friends, create pairs (a_i, b_i).
        # For a fixed total = t: count friends with a_i <= t <= b_i

        # To optimize, for each friend, a_i and b_i defines an interval [a_i, b_i].
        # Friend is okay if total is in that interval.

        # Sort intervals by a_i ascending
        # Then for total t, friends with a_i <= t is prefix of list

        # Then among prefix, count how many have b_i >= t.

        # So, we can:
        # Sort friends by a_i ascending
        # For b_i, we can keep a Fenwick tree or Balanced BST tracking counts of b_i

        # However, even simpler approach:

        self.friends.sort(key=lambda f: f.constraint.min_people)
        a_list = [f.constraint.min_people for f in self.friends]
        b_list = [f.constraint.max_people for f in self.friends]

        # We'll do a binary search on k = number of friends invited
        # For each k we check if possible

        def can_invite(k: int) -> bool:
            t = k + 1
            # Need at least k friends with a_i <= t <= b_i

            # find how many have a_i <= t
            # Using bisect_right because a_i <= t
            import bisect
            idx = bisect.bisect_right(a_list, t)
            # friends from 0 to idx-1 have a_i <= t

            # Among these, count how many have b_i >= t
            count = 0
            for i in range(idx):
                if b_list[i] >= t:
                    count +=1
            return count >= k

        # Binary search k in [0, N]
        low, high = 0, len(self.friends)
        result = 0
        while low <= high:
            mid = (low + high) // 2
            if can_invite(mid):
                result = mid
                low = mid +1
            else:
                high = mid -1
        return result


class InputParser:
    def __init__(self, input_lines):
        self.lines = input_lines
        self.index = 0

    def readline(self):
        line = self.lines[self.index]
        self.index += 1
        return line


class ProblemBSolver:
    def __init__(self, input_lines):
        self.parser = InputParser(input_lines)
        self.group = FriendGroup()

    def parse(self):
        N = int(self.parser.readline())
        for _ in range(N):
            a_str = self.parser.readline()
            a, b = map(int, a_str.split())
            constraint = RangeConstraint(a, b)
            friend = Friend(constraint)
            self.group.add_friend(friend)

    def solve(self):
        return self.group.max_invite()


def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    solver = ProblemBSolver(lines)
    solver.parse()
    print(solver.solve())


if __name__ == "__main__":
    main()