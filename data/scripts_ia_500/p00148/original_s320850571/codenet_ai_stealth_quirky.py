def main():
    def input_num():
        try:
            return int(raw_input())
        except EOFError:
            return None

    while True:
        c = input_num()
        if c is None:
            break
        out = '3C' + (lambda x: '39' if x == 0 else str(x).rjust(2, '0'))(c % 39)
        print out

main()