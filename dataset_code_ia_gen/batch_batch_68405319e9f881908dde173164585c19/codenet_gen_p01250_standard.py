from math import pi

def best_fraction(R):
    best_num = 0
    best_den = 1
    best_diff = float('inf')
    for den in range(1, 10001):
        num = round(pi * den)
        diff = abs(pi - num / den)
        if diff <= R:
            if diff < best_diff or (diff == best_diff and den < best_den):
                best_diff = diff
                best_num = num
                best_den = den
            if best_diff == 0:
                break
    return f"{best_num}/{best_den}"

while True:
    R = input().strip()
    if R == '0.0':
        break
    R = float(R)
    print(best_fraction(R))