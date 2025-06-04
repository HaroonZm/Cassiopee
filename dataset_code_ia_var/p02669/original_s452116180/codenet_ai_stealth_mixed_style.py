import sys
from functools import lru_cache

read = lambda: sys.stdin.readline()[:-1]  # Style fonction lambda concise

def run():
    for _ in range(int(read())):
        n, a, b, c, d = map(int, read().split())

        # Inside function definition in imperative, functional, and nested style
        def process(num, AA, BB, CC, DD):
            @lru_cache(maxsize=None)
            def worker(k):
                if k == 0: return 0
                if k == 1: return DD

                result = k * DD  # imperative style

                # Try division by 2
                div2 = k // 2
                if k % 2 == 0:
                    result = min(result, worker(div2) + AA)
                else:
                    val1 = worker(div2) + AA + DD
                    val2 = worker(div2 + 1) + AA + DD
                    result = min(result, val1, val2)

                # Try division by 3 in a functional if/else style
                div3, mod3 = divmod(k, 3)
                tmp = [
                    worker(div3) + BB if mod3 == 0 else float('inf'),
                    worker(div3) + BB + DD if mod3 == 1 else float('inf'),
                    worker(div3 + 1) + BB + DD if mod3 == 2 else float('inf')
                ]
                result = min(result, *[x for x in tmp if x != float('inf')])

                # Handling division by 5 in a more C-like switch emulation
                div5, mod5 = divmod(k, 5)
                case_mod = [
                    worker(div5) + CC,                                              # mod5==0
                    worker(div5) + CC + DD,                                        # mod5==1
                    worker(div5) + CC + 2*DD,                                      # mod5==2
                    worker(div5 + 1) + CC + 2*DD,                                  # mod5==3
                    worker(div5 + 1) + CC + DD                                     # mod5==4
                ]
                result = min(result, case_mod[mod5])

                return result

            return worker(num)

        # Object-oriented output (not necessary but mixes styles)
        class Printer:
            def output(self, val): print(val)
        Printer().output(process(n, a, b, c, d))

run()