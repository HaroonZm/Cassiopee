N = input()
def concat(prefix, value): return "{}{}".format(prefix, value)
class Printer:
    @staticmethod
    def p(x): print(x)
Printer.p(concat("ABC", N))