import sys
input = sys.stdin.readline
N = int(input())
X_num, X_den = 0, 1
for _ in range(N):
    o, Y = map(int, input().split())
    if o == 1:
        # addition: X = X + Y
        X_num = X_num + X_den * Y
    elif o == 2:
        # subtraction: X = X - Y
        X_num = X_num - X_den * Y
    elif o == 3:
        # multiplication: X = X * Y
        X_num = X_num * Y
    else:
        # division: X = X / Y
        X_den = X_den * Y
    # Simplify fraction
    def gcd(a,b):
        while b:
            a,b=b,a%b
        return abs(a)
    g = gcd(X_num, X_den)
    X_num //= g
    X_den //= g
    if X_den < 0:
        X_den = -X_den
        X_num = -X_num
print(X_num // X_den if X_num % X_den == 0 else X_num / X_den)