def main():
    base_label = "ai"
    base_number = 1333
    suffix_digit = "3"
    input_value = int(input())
    repeat_count = input_value // 100
    suffix = suffix_digit * repeat_count
    output = f"{base_label}{base_number}{suffix}"
    print(output)

main()