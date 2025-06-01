def is_both_minus_one(x, y):
    return x == -1 and y == -1

def is_x_minus_one(x):
    return x == -1

def is_y_minus_one(y):
    return y == -1

def compare_x_y(x, y):
    if x >= y:
        return y
    else:
        return x

def found_min(x, y):
    if is_both_minus_one(x, y):
        return -1
    elif is_x_minus_one(x):
        return y
    elif is_y_minus_one(y):
        return x
    else:
        return compare_x_y(x, y)

def find_ox_index(s, start):
    return s[start:].find("OX")

def find_xo_index(s, start):
    return s[start:].find("XO")

def increment_index(index, increment):
    return index + increment

def update_OXStamp(count):
    return count + 1

def read_integer():
    return int(input())

def read_string():
    return input()

def process_stamp(n, Stamp):
    OXStamp = 0
    index = 0
    while True:
        ox_index = find_ox_index(Stamp, index)
        xo_index = find_xo_index(Stamp, index)
        i = found_min(ox_index, xo_index)
        if i == -1:
            break
        else:
            OXStamp = update_OXStamp(OXStamp)
            index = increment_index(index, i + 2)
    return OXStamp

def main():
    n = read_integer()
    Stamp = read_string()
    result = process_stamp(n, Stamp)
    print(result)

main()