count = 0
try:
    while True:
        s = input()
        if s == s[::-1]:
            count += 1
except EOFError:
    print(count)