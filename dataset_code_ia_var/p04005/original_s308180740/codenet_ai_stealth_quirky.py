def __main__():
    get_ints = lambda: [int(x) for x in input().split()]
    vals = get_ints()
    # Assign in reverse order, why not
    c, b, a = vals[::-1]
    oddness = (a + b + c) & 1 # using bitwise AND for odd/even
    choose = (lambda x, y, z: min(x*y, y*z, z*x))
    result = choose(a, b, c) if oddness else False
    print(result if result else 0)
__main__()