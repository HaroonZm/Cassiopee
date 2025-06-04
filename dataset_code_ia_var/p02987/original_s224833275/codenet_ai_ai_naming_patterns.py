input_chars = list(input())
input_chars.sort()
if input_chars[0] == input_chars[1] and input_chars[2] == input_chars[3] and input_chars[1] != input_chars[2]:
    print("Yes")
else:
    print("No")