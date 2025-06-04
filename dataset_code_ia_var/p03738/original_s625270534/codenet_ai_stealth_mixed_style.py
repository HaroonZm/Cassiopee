A = int(input())
B = int(input())

def compare(a, b):
    if a > b:
        return 'GREATER'
    elif a < b:
        return 'LESS'
    return 'EQUAL'

result = (lambda f, x, y: f(x, y))(compare, A, B)
for r in [result]:
    print(r)