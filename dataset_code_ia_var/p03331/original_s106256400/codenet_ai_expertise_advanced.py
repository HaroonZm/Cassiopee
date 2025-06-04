match n := input():
    case '0':
        print(10)
    case _ if int(n) % 10 == 0:
        print(10)
    case _:
        print(sum(map(int, n)))