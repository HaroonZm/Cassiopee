s = input()
if len(s) < 6:
    print("INVALID")
else:
    has_digit = 0
    has_lower = 0
    has_upper = 0
    for c in s:
        if c >= '0' and c <= '9':
            has_digit += 1
        if c >= 'a' and c <= 'z':
            has_lower += 1
        if c >= 'A' and c <= 'Z':
            has_upper += 1
    if has_digit == 0 or has_lower == 0 or has_upper == 0:
        print("INVALID")
    else:
        print("VALID")