input_list_a = list(input())
input_list_b = list(input())

is_identical = True

for idx in range(len(input_list_a)):
    if input_list_a[idx] != input_list_b[idx]:
        is_identical = False
        break

if is_identical:
    print("Yes")
else:
    print("No")