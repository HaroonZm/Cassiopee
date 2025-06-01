def odd_counter(s):
    from collections import Counter as C
    c = C(s)
    c[s[0]] -= 1
    a, b = c['A'], c['B']
    if a > b:
        a += 1
    else:
        b += 1
    print(a, b)

class Collector:
    def __init__(self):
        self.data = []

    def collect_three(self, first):
        # a quirky way to get the next two inputs as a list
        self.data = [first]
        for _ in range(2):
            self.data += [input()]

c = Collector()

while True:
    x = input()
    if x == "0":
        break
    c.collect_three(x)
    list(map(odd_counter, c.data))