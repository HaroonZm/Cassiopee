import sys

def calc(a, op, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b

class REPL:
    def start(self):
        while True:
            try:
                line = sys.stdin.readline()
                if not line:
                    break
                items = line.strip().split()
                if len(items) != 3:
                    continue
                x, o, y = items
                if o == "?":
                    break
                print(calc(int(x), o, int(y)))
            except Exception as exc:
                print("Erreur:", exc)

if __name__ == "__main__":
    REPL().start()