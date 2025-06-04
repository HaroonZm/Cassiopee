def generate_patterned_output():
    base_string = "ai1333"
    repetition_count = int(input())
    suffix_string = "3" * (repetition_count // 100)
    print(base_string + suffix_string)

generate_patterned_output()