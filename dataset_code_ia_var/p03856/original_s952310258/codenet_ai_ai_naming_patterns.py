input_string = input().strip()
word_list = ['dream', 'dreamer', 'erase', 'eraser']
while True:
    replaced = False
    for word in word_list:
        if input_string.endswith(word):
            input_string = input_string[:-len(word)]
            replaced = True
            break
    if not replaced:
        break
print("YES" if not input_string else "NO")