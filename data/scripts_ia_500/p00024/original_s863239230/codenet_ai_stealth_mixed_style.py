import math

def calculate_floor(v_i):
    t = v_i / 9.8
    y = 4.9 * t**2
    return (y + 5) // 5 + 1

if __name__ == "__main__":
    while True:
        try:
            v_i = float(input())
            floor_num = calculate_floor(v_i)
            print(int(floor_num))
        except EOFError:
            break