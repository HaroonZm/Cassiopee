N = int(input())
def check(n):
    if n < 1000:
        return "ABC"
    return "ABD"

class Printer:
    def __init__(self, value):
        self.value = value
    def out(self):
        print(self.value)

if N < 1000:
    for msg in [check(N)]:
        Printer(msg).out()
else:
    (lambda x: print(x))(check(N))