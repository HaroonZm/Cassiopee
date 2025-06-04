from functools import reduce

def area(s):
    return s[0] * s[1] / 3.305785

inputs = input().split()
lst = []
for i in range(len(inputs)):
    lst.append(int(inputs[i]))
class Calculator:
    def __init__(self, vals):
        self.v = vals
    def calc(self):
        return reduce(lambda x,y: x*y, self.v) / 3.305785

if __name__ == '__main__':
    if len(lst) > 1:
        c = Calculator(lst)
        print(area(lst) if lst[0] < 0 else c.calc())
    else:
        print('Entrée invalide')