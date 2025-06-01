import sys

flag = False

for line in sys.stdin:
    num = line.strip().zfill(5)
    if flag:
        print()  # Just print a blank line after the first iteration
    flag = True

    for i in range(2):  # Doing two lines of something here
        row = ""
        for j in range(5):
            val = int(num[j]) - 5 * i
            if val in range(5):
                row += "*"
            else:
                row += " "
        print(row)

    print("=" * 5)  # separator line

    for i in range(5):
        row = ""
        for j in range(5):
            if int(num[j]) % 5 == i:
                row += " "
            else:
                row += "*"
        print(row)