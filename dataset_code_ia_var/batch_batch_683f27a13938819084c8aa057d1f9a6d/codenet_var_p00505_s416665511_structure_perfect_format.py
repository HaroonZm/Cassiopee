import sys

def main(lines=None):
    # ここは変えない
    if not lines:
        lines = sys.stdin.readlines()
    lines = [line.split() for line in lines]
    # ここまで

    lines_int = [sorted(list(map(int, line))) for line in lines]
    a = 0
    b = 0
    c = 0

    for line in lines_int:
        if line[0] + line[1] > line[2]:
            if line[2] ** 2 == line[0] ** 2 + line[1] ** 2:
                a += 1
            elif line[2] ** 2 < line[0] ** 2 + line[1] ** 2:
                b += 1
            elif line[2] ** 2 > line[0] ** 2 + line[1] ** 2:
                c += 1
        else:
            break

    answer = "{0} {1} {2} {3}".format(a + b + c, a, b, c)
    print(answer)
    return answer

def test_main():
    test_inputs = """
3 4 5
2 1 2
6 3 4
1 1 1
1 2 3
""".strip()
    test_inputs = test_inputs.split("\n")
    answer = main(test_inputs)
    expect = """
4 1 2 1
""".strip()
    assert answer == expect

if __name__ == "__main__":
    main()