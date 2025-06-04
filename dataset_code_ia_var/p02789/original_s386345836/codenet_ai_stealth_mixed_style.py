def main():
    get = lambda: [int(x) for x in input().split()]
    class Checker:
        def __init__(self, a, b): self.a = a; self.b = b
        def is_equal(self): return self.a == self.b
    n, m = get()
    c = Checker(n, m)
    if c.is_equal():
        result = "Yes"
    else:
        result = "No"
    print(result)
main()