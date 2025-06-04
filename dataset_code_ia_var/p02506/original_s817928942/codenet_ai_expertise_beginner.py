def solve():
    t = raw_input()
    total = 0
    while True:
        line = raw_input()
        if line == "END_OF_TEXT":
            print total
            return
        words = line.split()
        for word in words:
            if word.lower() == t:
                total += 1

solve()