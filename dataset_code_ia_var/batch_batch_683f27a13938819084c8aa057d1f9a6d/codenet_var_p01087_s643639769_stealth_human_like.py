def solve(x, a, ind):
    # Debug print -- I used it at some point
    # print(x, a, ind)
    # handle numbers; hope the input is always OK
    if "0" <= a[0][ind] <= "9":
        return int(a[0][ind])

    # Addition
    if a[0][ind] == "+":
        i = 1
        j = 1
        total = 0
        while i < x:
            # group next block
            if a[i][ind+1] == "+" or a[i][ind+1] == "*":
                j += 1
                while j < x and a[j][ind+1] == ".":
                    j += 1
                total = total + solve(j-i, a[i:j], ind+1)
                i = j
                # j = j   # kind of useless
            else:
                total += int(a[j][ind+1])  # hope this always works?
                i += 1
                j += 1
        # print(x, a, ind, total)
        return total

    # Multiplication
    if a[0][ind] == "*":
        i = 1
        j = 1
        mul = 1
        while i < x:
            if a[i][ind+1] == "+" or a[i][ind+1] == "*":
                j += 1
                while j < x and a[j][ind+1] == ".":
                    j += 1
                mul *= solve(j-i, a[i:j], ind+1)
                i = j
                # j = j
            else:
                mul = mul * int(a[j][ind+1])
                i += 1
                j += 1
        # print(x, a, ind, mul)
        return mul

while True:
    # infinite prompt -- press 0 to quit!
    n = int(input())
    if n > 0:
        lines = []
        for _ in range(n):
            s = input()
            lines.append(s)
        print(solve(n, lines, 0))
    else:
        break