class Dice:
    NS = [1, 5, 6, 2]
    EW = [1, 3, 6, 4]

    def __init__(self):
        self.reset_dice()

    def reset_dice(self):
        self.NS = [1, 5, 6, 2]
        self.EW = [1, 3, 6, 4]

    def question(self, top, front):
        self.handle_question(top, front)

    def handle_question(self, top, front):
        self.setTop(top)
        sides = self.get_sides()
        index = self.find_side_index(sides, front)
        result_index = self.calculate_result_index(index)
        value = self.get_value_from_sides(sides, result_index)
        return value

    def get_sides(self):
        return [self.NS[1], self.EW[1], self.NS[3], self.EW[3]]

    def find_side_index(self, sides, front):
        return sides.index(front)

    def calculate_result_index(self, index):
        return (index + 3) % 4

    def get_value_from_sides(self, sides, index):
        return sides[index]

    def setTop(self, n):
        if self.is_in_NS(n):
            self.setTop_via_NS(n)
        else:
            self.setTop_via_EW(n)

    def is_in_NS(self, n):
        return n in self.NS

    def setTop_via_NS(self, n):
        while not self.check_NS_top(n):
            self.N()

    def setTop_via_EW(self, n):
        while not self.check_NS_top(n):
            self.E()

    def check_NS_top(self, n):
        return self.NS[0] == n

    def N(self):
        self.rotate_NS()
        self.sync_EW_after_N()

    def rotate_NS(self):
        tail = self.NS.pop()
        self.NS.insert(0, tail)

    def sync_EW_after_N(self):
        self.EW[0] = self.NS[0]
        self.EW[2] = self.NS[2]

    def E(self):
        self.rotate_EW()
        self.sync_NS_after_E()

    def rotate_EW(self):
        tail = self.EW.pop()
        self.EW.insert(0, tail)

    def sync_NS_after_E(self):
        self.NS[0] = self.EW[0]
        self.NS[2] = self.EW[2]

def get_dice_numbers():
    return input().split()

def get_query_count():
    return int(input())

def get_query():
    return input().split()

def convert_face_to_index(dnum, face):
    return dnum.index(face) + 1

def print_answer(dnum, r):
    print(dnum[r - 1])

def process_queries():
    dnum = get_dice_numbers()
    n = get_query_count()
    for _ in range(n):
        t, f = get_query()
        result = get_query_result(dnum, t, f)
        print_answer(dnum, result)

def get_query_result(dnum, t, f):
    d = Dice()
    top_idx = convert_face_to_index(dnum, t)
    front_idx = convert_face_to_index(dnum, f)
    return d.question(top_idx, front_idx)

if __name__ == '__main__':
    process_queries()