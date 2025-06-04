class Element:
    def __init__(self, value):
        self.value = value

class Mapping:
    def __init__(self, domain, image):
        self.domain = domain
        self.image = image
        self.map_dict = {d.value: i.value for d, i in zip(domain, image)}

    def __call__(self, x):
        return self.map_dict[x.value]

    def set_value(self, x, val):
        self.map_dict[x.value] = val

    def values(self):
        return [self.map_dict[d.value] for d in self.domain]

class ProblemB:
    def __init__(self, N, a_list, b_list):
        self.N = N
        self.elements = [Element(v) for v in a_list]
        self.f = Mapping(self.elements, [Element(b) for b in b_list])
        self.b_inv_map = self._inverse_map()

    def _inverse_map(self):
        inv = {}
        for e in self.elements:
            fb = self.f(e)
            if fb in inv:
                inv[fb].append(e)
            else:
                inv[fb] = [e]
        return inv

    def check_condition(self):
        # The condition is equivalent to: f is injective.
        # Because for any x,y in S, if f(x)=f(y), then g(f(x))=g(f(y)) always true,
        # but if x!=y and f(x)=f(y), then can construct g,h such that g(f(x))=h(f(x)) but g(x) != h(x).
        # So we search for collisions in f.
        for val, pre_images in self.b_inv_map.items():
            if len(pre_images) > 1:
                return False, pre_images[0], pre_images[1]
        return True, None, None

    def construct_counterexample(self, x, y):
        # g(f(x))=h(f(x)) for all x but g(x)!=h(x) fails,
        # construct g,h mapping S->S.
        # Here x,y in S with f(x)=f(y).

        # Let's construct:
        # - g(u) = arbitrary but g(f(x)) = g(f(y)) = c
        # - h(u) = g(u) for all u except h(y) != g(y).
        # To satisfy g(f(x))=h(f(x)), we must have g(f(x))=h(f(x)).
        # Since f(x)=f(y), g(f(x))=g(f(y))=h(f(y)) => h(f(y))=g(f(y))
        # So for vertex v in image of f, g(v) = h(v)
        # We'll choose values for g and h on domain S so that
        # g(x) != h(x) for some x in S, contradicting the condition.

        # We'll assign g and h values carefully:
        # For all elements, initialize g and h mapping to their f(x) values to ensure no conflict in image space.
        g_vals = [self.f(e) for e in self.elements]
        h_vals = [self.f(e) for e in self.elements]

        # To cause difference, pick x and y with f(x) = f(y).
        # Change g(x) and h(x), g(y) and h(y) carefully:
        # We'll set g(x) = c (say f(x))
        # set h(x) = c (equal)
        # set g(y) = p
        # set h(y) = q distinct from p, but g(f(y)) = h(f(y)), which must hold,
        # so since f(x) = f(y), g(f(y)) = g(f(x)) = c and h(f(y)) = h(f(x)) = c, so g(f(y))=h(f(y))=c

        # We need to set g(y) != h(y), but g(f(y))=h(f(y)) still holds,
        # which is f(x), the same as f(y).
        # We'll set g(y) = an arbitrary value different from h(y), but all must be in S

        # We choose for simplicity:
        # g(x) = f(x)
        # h(x) = f(x)
        # g(y) = f(x) (same)
        # h(y) = different from f(x) (to make g(y) != h(y))

        # But g(y) != h(y) contradicts if g(y) = f(x), same as h(f(y)) = c, so no violation.

        # So instead, change g and h values on *domain* points, not in the image.

        # We'll assign:
        # g(x) = f(x)
        # h(x) = f(x)
        # For y:
        # g(y) = c1 != c2 = h(y),
        # But g(f(y))=h(f(y)) must hold,
        # so for f(y) = f(x), g(f(x)) = h(f(x)) = value.

        # To ensure this:
        # For the codomain elements, g and h must be equal on elements f(S)
        # So values assigned to g and h on codomain S must be consistent on f(S).
        # But g and h are defined on domain S. So no restriction on images of g and h on domain.

        # Thus, to force difference in g(y) and h(y), pick any c1 != c2 in S

        # Let's pick g(y) = f(x)
        # h(y) = a value different from f(x), e.g., for h(y), pick 1 if f(x) != 1 else 2

        # For all other elements, set g and h equal to f(x) or any valid value to satisfy conditions

        # Initialize g and h as copies of f over domain
        g_array = [self.f(e) for e in self.elements]
        h_array = [self.f(e) for e in self.elements]

        ix_x = self.elements.index(x)
        ix_y = self.elements.index(y)
        f_x_val = self.f(x)

        # assign g(y) = f_x_val
        g_array[ix_y] = f_x_val
        # assign h(y) a different value
        diff_val = 1 if f_x_val != 1 else 2
        h_array[ix_y] = diff_val

        return g_array, h_array

    def solve(self):
        condition_holds, x, y = self.check_condition()
        if condition_holds:
            print("Yes")
        else:
            g_vals, h_vals = self.construct_counterexample(x, y)
            print("No")
            print(' '.join(str(v.value) if isinstance(v, Element) else str(v) for v in g_vals))
            print(' '.join(str(v.value) if isinstance(v, Element) else str(v) for v in h_vals))

def main():
    import sys
    sys.setrecursionlimit(10**7)
    N = int(sys.stdin.readline())
    a_list = list(map(int, sys.stdin.readline().split()))
    b_list = list(map(int, sys.stdin.readline().split()))
    problem = ProblemB(N, a_list, b_list)
    problem.solve()

if __name__ == "__main__":
    main()