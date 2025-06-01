def main__():
    __input = input
    __map = map
    __split = str.split
    __format = "{0}".format
    chairs = list(__map(int, __input().__split()))
    __print = print
    __print(__format(chairs[0] * chairs[1]))

if __name__ == "__main__":
    main__()