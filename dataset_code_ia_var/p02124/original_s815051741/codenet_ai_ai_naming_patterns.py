ai_prefix = "ai"
ai_number = "1"
number_input = int(input())
multiplier_base = 3
multiplier_offset = 3
multiplier_value = number_input // 100 + multiplier_offset
suffix_string = str(multiplier_base) * multiplier_value
result_string = ai_prefix + ai_number + suffix_string
print(result_string)