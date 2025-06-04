def process():
    import sys
    def handle_line(line):
        """Procedural: Process individual string."""
        return line.replace('Hoshino', 'Hoshina')
    class Rep:
        def __init__(self, count):
            self.count = count
        def go(self):
            for _ in range(self.count):
                print(handle_line(next(inpt)))
    inpt = iter(sys.stdin.readline, '')
    while True:
        try:
            n = int(next(inpt))
        except:
            break
        r = Rep(n)
        r.go()
process()