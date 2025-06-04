from functools import reduce

stop = False
def weird_addition():
    global stop
    while not stop:
        try:
            stuff = [int(x) for x in input().split()]
            r = reduce(lambda x, y: x + y, stuff, 0)
            lens = len(str(r))
            print(lens)
        except Exception as something_bad_happened:
            stop = True

weird_addition()