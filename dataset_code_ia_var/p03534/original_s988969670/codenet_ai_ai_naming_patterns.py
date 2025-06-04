input_chars = list(input())
input_length = len(input_chars)
count_a = input_chars.count("a")
count_b = input_chars.count("b")
count_c = input_chars.count("c")

if input_length % 3 == 0:
    if count_a == count_b and count_b == count_c:
        print("YES")
    else:
        print("NO")
else:
    min_count = input_length // 3
    max_count = min_count + 1
    if min_count <= count_a <= max_count and min_count <= count_b <= max_count and min_count <= count_c <= max_count:
        print("YES")
    else:
        print("NO")