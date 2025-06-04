import sys
import math

def read_input():
    return sys.stdin.read().strip().split()

def parse_integers(values):
    return list(map(int, values))

def to_radians(degrees):
    return math.radians(degrees)

def law_of_cosines(a, b, angle_radians):
    return math.sqrt(a * a + b * b - 2 * a * b * math.cos(angle_radians))

def triangle_perimeter(a, b, c):
    return a + b + c

def semiperimeter(a, b, c):
    return (a + b + c) / 2

def heron_area(s, a, b, c):
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def triangle_height(area, base):
    return (area * 2) / base

def print_formatted(*values):
    for val in values:
        print('{0:.8f}'.format(val))

def main():
    inputs = read_input()
    a, b, angle = parse_integers(inputs)
    angle_radians = to_radians(angle)
    c = law_of_cosines(a, b, angle_radians)
    circum = triangle_perimeter(a, b, c)
    s = semiperimeter(a, b, c)
    area = heron_area(s, a, b, c)
    h = triangle_height(area, a)
    print_formatted(area, circum, h)

main()