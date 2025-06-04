import sys
from fractions import Fraction

def parse_angle(s):
    directions = ['north', 'west']
    angle = Fraction(0)
    segment = Fraction(90)
    idx = 0
    tokens = []
    while s:
        for d in directions:
            if s.endswith(d):
                tokens.append(d)
                s = s[:-len(d)]
                break
        idx += 1
    tokens = tokens[::-1]
    for depth, d in enumerate(tokens):
        if depth == 0:
            if d == 'north':
                angle = Fraction(0)
            else:
                angle = Fraction(90)
        else:
            segment /= 2
            angle += segment * (1 if d == 'west' else -1)
    return angle

def main():
    for line in sys.stdin:
        s = line.strip()
        if s == '#':
            break
        angle = parse_angle(s)
        if angle.denominator == 1:
            print(angle.numerator)
        else:
            print(f"{angle.numerator}/{angle.denominator}")

if __name__ == '__main__':
    main()