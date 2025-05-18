int_w, int_a, int_b = map(int, input().split())

if int_a <= (int_b) <= (int_a + int_w) or int_a <= (int_b + int_w) <= (int_a + int_w):
    print(0)
else:
    print(min([abs(a-b) for a in [int_a, int_a + int_w] for b in [int_b, int_b + int_w]]))