def main():
    def get_int(prompt='Give me a number: '):
        try:
            return int(input(prompt))
        except ValueError:
            return None

    class Counter:
        def __init__(self, start):
            self.val = start
            self.count = 0
        def bump_until(self, limit, step):
            while self.val <= limit:
                self.val += step
                self.count += 1

    while 1==1:
        n = get_int()
        if n == 0 or n is None:
            break
        c = Counter(n)
        c.bump_until(500, 500)
        c.bump_until(900, 100)
        c.bump_until(950, 50)
        c.bump_until(990, 10)
        c.bump_until(995, 5)
        c.bump_until(999, 1)
        print(c.count)

if __name__ == "__main__": main()