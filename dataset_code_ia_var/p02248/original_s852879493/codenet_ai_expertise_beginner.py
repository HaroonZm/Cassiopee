text = input()
pattern = input()

i = 0
while i <= len(text) - len(pattern):
    if text[i:i + len(pattern)] == pattern:
        print(i)
    i = i + 1