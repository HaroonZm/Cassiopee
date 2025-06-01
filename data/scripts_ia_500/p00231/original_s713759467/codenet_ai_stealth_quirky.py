import sys

class DangerousBridge:
    def __init__(self):
        self.limit = 150
        self.records = []

    def add_event(self, m, a, b):
        self.records.append((a, m))
        self.records.append((b, -m))

    def test_weight(self):
        total = 0
        for _, m in sorted(self.records):
            total += m
            if total > self.limit:
                return 'NG'
        return 'OK'

def mainloop(_):
    DB = DangerousBridge()
    while True:
        try:
            n = int(input())
            if n == 0:
                break
            DB.records.clear()
            for __ in range(n):
                m,a,b = map(int,input().split())
                DB.add_event(m,a,b)
            print(DB.test_weight())
        except EOFError:
            break

if __name__ == '__main__':
    mainloop(sys.argv)