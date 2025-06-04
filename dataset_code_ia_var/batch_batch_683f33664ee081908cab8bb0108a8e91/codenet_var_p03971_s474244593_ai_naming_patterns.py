total_length, max_a, max_b = map(int, input().split())
candidate_string = input()
current_total = 0
current_b = 0
for idx in range(total_length):
    char = candidate_string[idx]
    if char == "a":
        if current_total < max_a + max_b:
            print("Yes")
            current_total += 1
        else:
            print("No")
    elif char == "b":
        if current_total < max_a + max_b and current_b < max_b:
            print("Yes")
            current_total += 1
            current_b += 1
        else:
            print("No")
    else:
        print("No")