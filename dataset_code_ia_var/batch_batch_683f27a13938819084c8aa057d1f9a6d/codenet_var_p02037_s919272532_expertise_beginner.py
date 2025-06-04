h, w = input().split()
h = int(h)
w = int(w)

a, b = input().split()
a = int(a)
b = int(b)

rectangles_in_h = h // a
rectangles_in_w = w // b

total_cells = h * w
covered_cells = rectangles_in_h * rectangles_in_w * a * b

result = total_cells - covered_cells

print(result)