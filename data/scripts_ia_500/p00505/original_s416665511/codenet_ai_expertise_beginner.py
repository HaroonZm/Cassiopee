import sys

def main(lines=None):
    if lines == None:
        lines = sys.stdin.readlines()

    a = 0
    b = 0
    c = 0

    for line in lines:
        parts = line.split()
        nums = []
        for p in parts:
            nums.append(int(p))
        nums.sort()
        x = nums[0]
        y = nums[1]
        z = nums[2]

        if x + y > z:
            if z*z == x*x + y*y:
                a = a + 1
            elif z*z < x*x + y*y:
                b = b + 1
            else:
                c = c + 1
        else:
            break

    total = a + b + c
    print(str(total) + " " + str(a) + " " + str(b) + " " + str(c))
    return str(total) + " " + str(a) + " " + str(b) + " " + str(c)

def test_main():
    input_lines = [
        "3 4 5",
        "2 1 2",
        "6 3 4",
        "1 1 1",
        "1 2 3"
    ]
    result = main(input_lines)
    expected = "4 1 2 1"
    assert result == expected

if __name__ == "__main__":
    main()