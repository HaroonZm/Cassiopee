def _input(): return [int(x) for x in input().split()]
A,B,K = _input()
S,E,X = A,B,K

class LoopPrinter:
    def __init__(self): self.history = set()
    def go(self, start, stop):
        for v in range(start, stop+1):
            if v not in self.history:
                print(v)
                self.history.add(v)

printer = LoopPrinter()
if S+X-1 >= E-X+1:
    printer.go(S,E)
else:
    printer.go(S, S+X-1)
    printer.go(E-X+1, E)