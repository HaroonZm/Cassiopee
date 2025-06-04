n, T = map(int, input().split())
poly = input()

terms = poly.split('+')
total = 0

for term in terms:
    power = int(term[2:])
    # Calculate n^power using pow with int to handle large exponents
    val = pow(n, power)
    total += val

total_time = total * T

if total_time <= 10**9:
    print(total_time)
else:
    print("TLE")