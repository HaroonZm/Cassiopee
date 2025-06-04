import math

def get_input():
    return input()

def to_float(s):
    return float(s)

def area_of_circle(radius):
    return radius * radius * math.pi

def circumference_of_circle(radius):
    return 2 * radius * math.pi

def format_number(num):
    return "%.10f" % num

def compose_output(area, circumference):
    return f"{area} {circumference}"

def main():
    r_str = get_input()
    r = to_float(r_str)
    area = area_of_circle(r)
    circumference = circumference_of_circle(r)
    area_str = format_number(area)
    circumference_str = format_number(circumference)
    output = compose_output(area_str, circumference_str)
    print(output)

main()