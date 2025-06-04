def weirdStyle():
    from operator import mul
    from functools import reduce
    get_numbers = lambda: [*map(int, input().split())]
    A, B, C = get_numbers()
    MMM = (lambda *args: max(args))(A, B, C)
    result = {0: lambda: 0, 1: lambda: reduce(mul, [A,B,C])//MMM}[MMM%2!=0]()
    print(result)
weirdStyle()