n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

def division(x, y): return x / y

class MaxFinder:
    @staticmethod
    def find(x, y): return max(x, y)

def compute_final(n, a, b, c, d):
    temp1 = division(a, c)
    temp2 = b // d if d else 0
    greatest = MaxFinder.find(temp1, temp2)
    return int(n - greatest)

result = compute_final(n, a, b, c, d)
print(result)