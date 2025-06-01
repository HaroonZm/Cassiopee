while True:
    input_integer = int(input())
    if input_integer == -1:
        break
    point_complex = 1 + 0j
    for _ in range(input_integer - 1):
        direction_complex = point_complex * 1j
        direction_complex /= abs(direction_complex)
        point_complex += direction_complex
    print("{:.2f}\n{:.2f}".format(point_complex.real, point_complex.imag))