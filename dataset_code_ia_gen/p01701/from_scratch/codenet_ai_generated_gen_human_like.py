from fractions import Fraction

def parse_direction(direction):
    # Base cases
    if direction == "north":
        return Fraction(0, 1)
    if direction == "west":
        return Fraction(90, 1)
    # count total occurrences of 'north' and 'west'
    count = direction.count("north") + direction.count("west")
    # strip the first 'north' or 'west' to get the suffix direction
    if direction.startswith("north"):
        suffix = direction[5:]
        base_angle = parse_direction(suffix)
        return base_angle - Fraction(90, 2**count)
    elif direction.startswith("west"):
        suffix = direction[4:]
        base_angle = parse_direction(suffix)
        return base_angle + Fraction(90, 2**count)

while True:
    direction = input().strip()
    if direction == "#":
        break
    angle = parse_direction(direction)
    if angle.denominator == 1:
        print(angle.numerator)
    else:
        print(f"{angle.numerator}/{angle.denominator}")