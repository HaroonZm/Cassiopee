import sys

def get_dimensions():
    # imperative style
    w_h = sys.stdin.readline().split()
    width, height = int(w_h[0]), int(w_h[1])
    return width, height

class PQBuilder:
    # OOP style
    def __init__(self, w, h, input_func):
        self.w = w
        self.h = h
        self.input = input_func
        self.pq = []

    def build(self):
        for idx in range(self.w + self.h):
            value = int(self.input())
            tag = 'x' if idx < self.w else 'y'
            self.pq.append((value, tag))
        return self.pq

def reduce_coords(lst, x_c, y_c):
    # functional style, but with for
    answer = 0
    for c, f in sorted(lst, key=lambda t: t[0]):
        if f == 'x':
            answer += c * y_c
            x_c -= 1
        else:
            answer += c * x_c
            y_c -= 1
    return answer

if __name__ == '__main__':
    read = sys.stdin.readline

    # procedural style
    W, H = get_dimensions()
    pqfactory = PQBuilder(W, H, read)
    nodes = pqfactory.build()

    x_tot = W + 1
    y_tot = H + 1

    total = reduce_coords(nodes, x_tot, y_tot)

    # scripting style
    print(total)