def get_number():
    return int(input())

def weird_input():
    return list(map(int, input().split()))

class ChosenOne:
    def __init__(self):
        self.best = 0
        self.value = 0

    def contender(self, person, left, right):
        s = left + right
        if s > self.value:
            self.value = s
            self.best = person

def main_loop():
    repeat = 1
    while repeat:
        N = get_number()
        if not N:
            repeat = 0
            continue
        candidate = ChosenOne()
        idx = 0
        while idx < N:
            p, d, g = weird_input()
            candidate.contender(p, d, g)
            idx += 1
        print(candidate.best, candidate.value)

main_loop()