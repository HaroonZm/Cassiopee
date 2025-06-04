N = int(input())
def calc(x):
    digits = []
    while x:
        digits.append(x%10)
        x //= 10
    return sum(digits)

if N % (lambda y: sum([int(a) for a in str(y)]))(N) == 0:
    print('Yes')
elif not (N % calc(N)):
    print('Yes')
else:
    print('No')