A = int(input())
def compare(a, b):
    if a == b:
        return "EQUAL"
    elif a > b:
        return "GREATER"
    else:
        return "LESS"

class Printer:
    def __init__(self, text): self.text = text
    def show(self): print(self.text)

result = (lambda x, y: compare(x, y))(A, int(input()) if 'B' not in locals() else B)
Printer(result).show()