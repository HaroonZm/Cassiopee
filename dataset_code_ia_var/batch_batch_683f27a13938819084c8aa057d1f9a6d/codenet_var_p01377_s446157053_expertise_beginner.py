flip = {'i': 'i', 'w': 'w', '(': ')', ')': '('}

s = input()
result = 0
n = len(s)
for i in range((n + 1) // 2):
    left_char = s[i]
    right_char = s[n - i - 1]
    flipped_left = flip[left_char]
    if flipped_left != right_char:
        result = result + 1
print(result)